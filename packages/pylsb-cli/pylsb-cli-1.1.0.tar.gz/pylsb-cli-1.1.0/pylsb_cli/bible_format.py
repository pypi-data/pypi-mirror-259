"""Various text formatting utilities for PyLSB."""

__version__ = '1.0.0'

import re
from dataclasses import dataclass
from typing import Union

from pylsb.bible import BibleMarker, BibleRange
from pylsb.data import BOOKS, TITLES

ANSI_ESCAPES = re.compile(r'\x1b\[[0-9;]*m')
ESC = '\033'


def chapter_label(book: str, chapter_: int):
    """Create formatted Book Chapter string."""
    book = (f'{book[0]} {book[1:]}' if book[0].isdigit() else book).title()
    return f'{book} {chapter_}'


def bible_label(_s: Union[BibleMarker, BibleRange]):
    """Stringify a BibleMarker or Range."""
    if isinstance(_s, BibleMarker):
        return f'{chapter_label(_s.book, _s.chapter)}:{_s.verse}'
    return (
        f'{bible_label(_s.start)}-'
        f"{'' if _s.start.chapter == _s.end.chapter else f'{_s.end.chapter}:'}"
        f'{_s.end.verse}'
        if _s.start.book == _s.end.book
        else f'{bible_label(_s.start)} - {bible_label(_s.end)}')


def centered(width: int, text: str, prefix: str = '') -> str:
    """Tab out text based on given width, with optional prefix."""
    tab = width // 2 - len(text) // 2
    return f"{' ' * tab}{prefix}{text}"


def headings(
    mark: BibleMarker,
    data: dict,
    width: int,
    web: bool
) -> str:
    """Print heading, subheading, and acrostic letter of a verse."""
    res = ''
    screen = width
    width = width if web or width <= 30 else width * 2 // 3
    if data['heading']:
        if mark.verse > 1:
            res += '\n'
        line = data['heading']
        _l = ''
        for word in line.upper().split() if web else line.split():
            line = line if _l else ''
            if len(f'{_l}{word}') <= width:
                if _l:
                    _l += ' '
                _l += word
            else:
                line += f'{_l}\n' if web else centered(
                    screen,
                    f'{_l}\n',
                    '\033[0;1;3m')
                _l = word
        line += _l if web else centered(screen, _l, '\033[0;1;3m')
        res += f'{line}\n'
    if data['subheading']:
        line = data['subheading']
        _l = ''
        # The \e[0m is a sneaky way to factor our indenation into the output
        # since split would remove the spaces
        for word in f'\033[0m{line}'.split(' ') if web else line.split():
            line = line if _l else ''
            if len(f'{_l}{word}') < width:
                if _l:
                    _l += ' '
                _l += word
            else:
                line += f'{_l}\n' if web else centered(
                    screen,
                    f'{_l}\n',
                    '\033[0m')
                _l = word
        line += _l if web else centered(screen, _l, '\033[0m')
        res += (f'    {line[4:]}' if web else line) + '\n'
    if 'acrostic' in data['attributes']:
        letter = [
            _a
            for _a in data['attributes']
            if _a.startswith('acrostic#')][0].split('#')[1]
        res += (
            f'\n    \033[1m{letter}'
            if web
            else centered(screen, letter, '\033[0;31m')) + '\n'
    return res


def line_is_one_of(_a: str, idx: int, attrs: list[str]) -> tuple[bool, str]:
    """Check if a line is part of a certain category.

    If the attribute _a is found in the list attrs, this will then check if
    there is an attribute string equal to _a + '#' + idx. If there is, this
    function returns True, in all other cases it returns False.
    """
    found = [
        attr.split('#')[2] or ''
        for attr in attrs
        if attr.startswith(f'{_a}#{idx}')]
    return (True, found[0]) if found else (False, '')


@dataclass
class MarginInfo:
    """For internal use."""

    margin: str
    quote: bool
    space: int
    length: int


def __finalize_margin(
    info: MarginInfo,
    idx: int,
    attrs: list[str],
    web: bool,
    width: int
):
    """Determine additional margin and screen space."""
    # 2 Spaces between verse number and text, except for verses starting with
    # quotes
    info.quote, _ = line_is_one_of('quote', idx, attrs)
    if not info.quote:
        info.margin += ' '
    # Text body margin - poetry is offset 2 spaces to the right
    poetry, _ = line_is_one_of('poetry', idx, attrs)
    if poetry:
        info.margin += '  '
    indent, times = line_is_one_of('indent', idx, attrs)
    if indent:
        info.margin += ' ' * ((2 * int(times)) if web else 2)
    info.length = len(ANSI_ESCAPES.sub(
        '',
        info.margin)) + (2 if info.quote else 1)
    info.space = width - info.length


def verse(
    mark: BibleMarker,
    data: dict,
    width: int,
    nored: bool,
    web: bool
):
    """Display a verse on the screen, formatted for the terminal width."""
    res = ''
    info = MarginInfo('', False, 0, 0)
    highlight = int(
        ([
            _x
            for _x in data['attributes']
            if _x.startswith('highlight#')] or ['highlight#0'])[0]
        .split('#')[1])
    highlight = (
        '49'
        if highlight == 0
        else f'4{highlight}'
        if 0 < highlight < 8
        else f'48;5;{highlight}'
        if highlight > 7
        else (
            f'48;2;{-highlight // (256 * 256)};{(-highlight // 256) % 256};'
            f'{highlight % 256}'))
    for idx, line in enumerate(data['text']):
        info.margin = ''
        # Print headings, add ANSI attributes for special verses, and add verse
        # number
        if idx == 0:
            res += headings(mark, data, width, web)
            if 'break' in data['attributes']:
                res += '\033[0m\n'
            first = mark.verse == 1
            number = (
                mark.verse
                if not first or mark.book == 'psalm'
                else mark.chapter)
            # 4 lines below, commentated:
            # - begin by resetting attributes, add spacing before number
            # - make number red if beginning of chapter and not a psalm
            # - make bold and underlined if beginning of a paragraph
            # - print number and revert ANSI changes
            info.margin += (
                f"\033[0m{' ' * (3 - len(str(number)))}\033["
                f"{'31' if first and mark.book != 'psalm' and not web else ''}"
                f"{';1;4' if 'paragraph' in data['attributes'] else ''}"
                f'm{number}\033[39;22;24m')
        # Empty margin for EVERYTHING else
        else:
            info.margin += '   '
        __finalize_margin(info, idx, data['attributes'], web, width)
        info.margin += '\033[0m '
        # Remove red text if requested
        if nored:
            line = line.replace('\033[31m', '')
        # Split lines for screen space
        output = ''
        red = False
        for word in line.split() + (
            ['Selah.']
            if web and line_is_one_of('selah', idx, data['attributes'])[0]
            else []
        ) + (
            ['Higgaion Selah.']
            if web and line_is_one_of(
                'higgaion-selah',
                idx,
                data['attributes'])[0]
            else []
        ):
            if word.startswith('\033[31m'):
                red = True
            if word.endswith('\033[39m'):
                red = False
            # Add word to line
            if len(ANSI_ESCAPES.sub(
                '',
                f'{info.margin}{output}{word}'
            )) <= info.space:
                if output:
                    output += ' '
                output += word
            # Print line and begin a new one
            else:
                res += f'{info.margin}\033[{highlight}m{output}\033[49m\n'
                # After we've printed the first sub-line, we want to have a
                # blank margin (there will always be at least \e[0m to begin)
                if '\033' in info.margin:
                    info.margin = ' ' * info.length
                output = ('\033[31m' if red else '') + word
        res += (
            f"{info.margin}\033[{'31;' if red else ''}{highlight}m{output}"
            '\033[49m\n'
        ) + (
            '' if web else ((
                f"{' ' * (width - 6)}Selah.\n"
                if line_is_one_of('selah', idx, data['attributes'])[0]
                else ''
            ) + (
                f"{' ' * (width - 15)}Higgaion Selah.\n"
                if line_is_one_of('higgaion-selah', idx, data['attributes'])[0]
                else ''
            )))
    return res


def chapter(book: str, chapter_: int, start: bool, width: int, web: bool):
    """Print a chapter header/introduction.

    book and chapter self explanatory. start indicates whether or not verse 1
    is being printed too (only then do we typically print). width is the screen
    width. And web is whether or not to format like the website vs print.
    """
    res = ''
    if chapter_ == 1 and start:
        for head in TITLES[BOOKS.index(book)].split('\n'):
            italic = ';3' if head[-1].islower() else ''
            if web:
                if italic:
                    continue
                if book == 'psalm':
                    head = 'PSALM'
                head += ' 1'
                italic = ';39;23;1'
            res += (
                f"\033[31{italic}m"
                f"{' ' * (width // 2 - len(head) // 2)}"
                f"{head}\033[39;23;22m\n")
    elif book == 'psalm':
        head = f'PSALM {chapter_}'
        res += (
            f"\033[{39 if web else 31}m"
            f"{' ' * (width //  2 - len(head) // 2)}"
            f"{head}\033[39m\n")
    return res
