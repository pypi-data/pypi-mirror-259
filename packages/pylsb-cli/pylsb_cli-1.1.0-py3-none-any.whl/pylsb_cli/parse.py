"""Functions related to parsing command line arguments."""

__version__ = '1.0.0'

import argparse
import sys
from typing import Union

from pylsb.bible import BibleGetter, BibleMarker, BibleRange
from pylsb.parse import get_scripture

def get_highlight(val: str) -> int:
    """Parse a string as either a 1-3 digit integer, or a 6 digit hex value."""
    val = val.strip()
    if val.startswith('-'):
        raise argparse.ArgumentTypeError('color must be a positive value')
    if len(val) < 4:
        return int(val)
    if len(val[2:] if val.startswith('0x') else val) != 6:
        raise argparse.ArgumentTypeError('color should be 1, 2, 3 or 6 digits')
    return -int(val, 16)


def args(bible: BibleGetter) -> list[Union[BibleMarker, BibleRange]]:
    """Parse sys.argv into Scripture and options."""
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] scripture [scripture ...]',
        description=(
            'Downloads, displays, and caches verses '
            'from the Legacy Standard Bible'),
        epilog=(
            'The scripture references and options '
            'may be passed in any order.'))
    parser.add_argument(
        'scripture',
        action='store',
        help=(
            'chapter, verse, range of chapters or verses, '
            'or "random" for a random verse'),
        nargs='+',
        type=lambda _s: get_scripture(_s.lower(), bible))
    parser.add_argument(
        '-p',
        '--paragraph',
        action='store_true',
        help='expand a verse or range to include the whole paragraph')
    parser.add_argument(
        '-r',
        '--redownload',
        action='store_true',
        help='force a cache update even if the verses are already downloaded')
    parser.add_argument(
        '-n',
        '--nored',
        action='store_true',
        help='disable red text quotes')
    parser.add_argument(
        '-8',
        '--80columns',
        action='store_true',
        help='force width to 80 columns (ignore terminal settings)',
        dest='columns80')
    parser.add_argument(
        '-w',
        '--web',
        action='store_true',
        help='format text like the web version instead of the print version')
    parser.add_argument(
        '-b',
        '--browser',
        action='store_true',
        help='open scripture in web browser')
    parser.add_argument(
        '-f',
        '--preface',
        action='store_true',
        help='display preface before scripture')
    parser.add_argument(
        '-m',
        '--highlight',
        action='store',
        help=(
            'highlight all selected verses with specified color num '
            '(0 to remove)'),
        metavar='color',
        type=get_highlight)
    parser.add_argument(
        '-2',
        '--split',
        action='store_true',
        help='print verses in 2 columns, one screen at a time')
    return parser.parse_args(sys.argv[1:])
