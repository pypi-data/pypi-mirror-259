"""Runnable pylsb CLI code."""

import os
import re
import shutil
import sys
from typing import Union

from pylsb.bible import BibleGetter, BibleMarker, BibleRange

from pylsb_cli import bible_format
from pylsb_cli.parse import args as parse_args


def read_scripture(
    bible: BibleGetter,
    requests: list[Union[BibleMarker, BibleRange]],
    redownload: bool
) -> list[Union[str, dict]]:
    """Retrieve a list of Bible references from the database."""
    ret = []
    for _s in requests:
        res = bible.get(_s, redownload)
        if res:
            ret.append(bible_format.bible_label(_s))
            ret.append(res)
        else:
            print(
                "Invalid Bible " +
                ('verse' if isinstance(_s, BibleMarker) else 'verses') +
                f": {bible_format.bible_label(_s)}\n")
    return ret


# NOTE: this is hardcoded based on bible_format.py, so consider finding a
# better way...
HEADER_REGEX = re.compile(r'^(\s*\x1b\[0;1;3m)?[A-Z]')


def main():
    """Command line entry point."""
    # Scripture cache
    cache_dir = os.getenv('XDG_CACHE_HOME') or os.path.expanduser('~/.cache')
    if sys.platform == 'win32':
        cache_dir = f"{os.environ['LOCALAPPDATA']}/PyLSB"
        os.system("")  # Stupid Windows thing to make ANSI escape work
    os.makedirs(cache_dir, exist_ok=True)
    # Live data
    bible = BibleGetter(f'{cache_dir}/lsbible.json')

    # Selected Scriptures to print
    args = parse_args(bible)
    scriptures = args.scripture

    # Display preface
    if args.preface:
        print("Foreword to the LSB: https://lsbible.org/foreword/")
    # If they want paragraphs, expand each range
    if args.paragraph:
        for idx, _s in enumerate(scriptures):
            if not bible.valid(_s):
                continue
            start = bible.find_attribute_backwards(
                _s if isinstance(_s, BibleMarker) else _s.start,
                'paragraph',
                True,
                args.redownload)
            end = bible.find_attribute_forwards(
                _s if isinstance(_s, BibleMarker) else _s.end,
                'paragraph',
                False,
                args.redownload)
            if start != end:
                scriptures[idx] = BibleRange(start, end)
    # Get the data
    outputs = read_scripture(bible, scriptures, args.redownload)
    bible.save()
    if not outputs:
        print("No valid Scripture specified.")
        sys.exit(1)
    shutil.get_terminal_size((80, 20))
    width, height = (80, 25) if args.columns80 else os.get_terminal_size()
    if args.split:
        width = (width - 3) // 2
    res = ''
    for result in outputs:
        if isinstance(result, str):
            for i in range(0, len(result), width):
                res += f'{result[i:i + width]}\n'
        else:
            for book in list(result.keys()):
                for chapter in list(result[book].keys()):
                    res += bible_format.chapter(
                        book,
                        chapter,
                        1 in result[book][chapter],
                        width,
                        args.web)
                    for verse in list(result[book][chapter].keys()):
                        if args.highlight is not None:
                            bible.highlight(
                                book,
                                chapter,
                                verse,
                                args.highlight)
                        res += bible_format.verse(
                            BibleMarker(book, chapter, verse),
                            result[book][chapter][verse],
                            width,
                            args.nored,
                            args.web)
            res += '\n'
    bible.save()

    if args.split:
        # Break apart into one string per line - list
        lines = res.split('\n')
        while lines[-1].strip() == '':
            lines.pop()
        # Insert empty lines to make sure all headers are followed by at least
        # one verse - in other words, if there's a header followed by the edge
        # of the screen, we push it into the next column
        _i = 0
        while True:
            if _i >= len(lines):
                break
            if (
                lines[_i]
                and _i % ((height - 1) * 2) in {
                    height - 2,
                    ((height - 1) * 2 - 1)}
            ):
                _n = 0
                while HEADER_REGEX.search(lines[_i]):
                    _n += 1
                    _i -= 1
                for _ in range(0, _n):
                    lines.insert(_i, '')
            _i += 1
        # Where the printing happens - first loop through each set of (screen
        # height * 2) lines. We subtract 1 because we want to leave room for
        # the dividing bar (or maybe in the future, a "push any key" prompt for
        # pagination).
        started = False
        for _s in range(0, len(lines), (height - 1) * 2):
            # If there is a screen's worth of text already behind us, add a divider
            if started:
                print(f"\033[0m{'─' * (width + 1)}┼{'─' * (width + 1)}")
            started = True
            # Print 2 columns of lines
            for _i in range(_s, _s + height - 1):
                if _i < len(lines):
                    # Left side
                    _l1 = lines[_i] + ' ' * (
                        width - len(bible_format.ANSI_ESCAPES.sub(
                            '', lines[_i])))
                    # Right side
                    _l2 = (
                        lines[_i + height - 1]
                        if _i + height < len(lines)
                        else '')
                    print(f'{_l1}\033[0m │ {_l2}\033[0m')
    else:
        print(res)

if __name__ == "__main__":
    main()
