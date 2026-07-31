"""Paranoid text spacing for good readability.

Automatically insert whitespace between CJK (Chinese, Japanese, Korean) and
half-width characters (alphabetical letters, numerical digits and symbols).

>>> import pangu
>>> pangu.spacing_text("當你凝視著bug，bug也凝視著你")
'當你凝視著 bug，bug 也凝視著你'
>>> pangu.spacing_file("path/to/file.txt")  # doctest: +SKIP
'與 PM 戰鬥的人，應當小心自己不要成為 PM'
"""

import argparse
import sys

from pangu._core import has_proper_spacing, spacing_file, spacing_text

__version__ = "5.0.0"
__all__ = ["__version__", "cli", "has_proper_spacing", "spacing_file", "spacing_text"]


def cli(args: list[str] | None = None) -> None:
    """Transitional v4-style CLI; replaced by the argparse js-parity CLI in pangu._cli."""
    if not args:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="pangu",
        description=(
            "pangu.py -- Paranoid text spacing for good readability, to automatically insert whitespace between CJK and half-width characters (alphabetical letters, numerical digits and symbols)."
        ),
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("-t", "--text", action="store_true", dest="is_text", required=False, help="specify the input value is a text")
    parser.add_argument("-f", "--file", action="store_true", dest="is_file", required=False, help="specify the input value is a file path")
    parser.add_argument("text_or_path", action="store", type=str, help="the text or file path to apply spacing")

    if not sys.stdin.isatty():
        print(spacing_text(sys.stdin.read()))
    else:
        parsed_args = parser.parse_args(args)
        if parsed_args.is_text:
            print(spacing_text(parsed_args.text_or_path))
        elif parsed_args.is_file:
            print(spacing_file(parsed_args.text_or_path))
        else:
            print(spacing_text(parsed_args.text_or_path))
