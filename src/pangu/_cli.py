"""Command-line interface: flag-parity with pangu.js (src/node/cli.ts) plus Python-only stdin piping.

Deliberate deviations from the js CLI, all user-facing and documented in README:

- usage errors exit 2 (argparse convention) where js exits 1
- an explicit argument wins over piped stdin; stdin is read only when no argument
  is given (the rule pangu.js issue #309 adopts)
- ``-c`` composes with piped stdin
"""

import argparse
import os
import sys
from collections.abc import Sequence

from pangu._core import spacing_file, spacing_text


def _build_parser() -> argparse.ArgumentParser:
    from pangu import __version__  # noqa: PLC0415 import-outside-top-level — the package root imports this module, so the top level would be circular

    parser = argparse.ArgumentParser(
        prog="pangu",
        description=(
            "pangu.py -- Paranoid text spacing for good readability, to automatically insert whitespace between CJK and half-width characters (alphabetical letters, numerical digits and symbols)."
        ),
    )
    # self-identifying so `pangu -v` disambiguates from pangu.js when both are installed
    parser.add_argument("-v", "--version", action="version", version=f"pangu.py {__version__}")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-t", "--text", action="store_true", dest="is_text", help="treat the input as text (default)")
    mode.add_argument("-f", "--file", action="store_true", dest="is_file", help="treat the input as a file path")
    mode.add_argument("-c", "--check", action="store_true", dest="is_check", help="check whether the input already has proper spacing (exit 0 if yes, 1 if no)")
    parser.add_argument("text_or_path", nargs="?", help="the text or file path to apply spacing; reads stdin when omitted and piped")
    return parser


def _print_spacing(text: str) -> int:
    try:
        print(text)
    except BrokenPipeError:
        # `pangu -f big.txt | head` — point stdout at devnull so the interpreter's
        # shutdown flush does not raise a second time and stack-trace
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        return 1
    return 0


def cli(argv: Sequence[str] | None = None) -> int:
    """Run the pangu CLI and return its exit code."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.text_or_path is not None:
        source = args.text_or_path
    elif args.is_file:
        # a file path must be an explicit argument; stdin only ever carries text
        parser.error("the -f/--file option requires a file path argument")
    elif not sys.stdin.isatty():
        source = sys.stdin.read()
    else:
        parser.error("the following arguments are required: text_or_path (or pipe text via stdin)")

    new_text = spacing_file(source) if args.is_file else spacing_text(source)

    if args.is_check:
        if new_text == source:
            return 0
        print(f"Corrected: {new_text}", file=sys.stderr)
        return 1

    return _print_spacing(new_text)
