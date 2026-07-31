# Changelog

## v5.0.0 / 2026-08-01

- Implement **Paranoid Text Spacing Algorithm v9** (ported from [pangu.js](https://github.com/vinta/pangu.js) `v9.1.0`)
- Support Python 3.11+
- Fully type-annotated (`py.typed`)
- Add a method: `pangu.has_proper_spacing()`
- Add a command-line tool: `pangu-py` (an alias of the original `pangu`, to avoid a name collision)
- Add a CLI option: `-c/--check`, which exits 0 if the text has proper spacing, 1 if not
- Add an `encoding` parameter to `spacing_file()`, which now reads files as UTF-8 by default
- Remove `pangu.spacing()`, use `pangu.spacing_text()`

## v5.0.0 / 2026-07-31

Port of the pangu.js v9 text-spacing engine — same algorithm, same behavior, parity-locked by a 1:1 port of the pangu.js test suite.

Breaking changes:

- Half-width punctuation is no longer converted to full-width. The only conversions left: a colon in direct CJK contact right before parentheses becomes `：`, and middle dots (`·` `•` `‧`) normalize to `・`. There is no flag to restore the old behavior
- `pangu.spacing()` is removed; use `pangu.spacing_text()`
- Output is no longer stripped of leading/trailing whitespace
- `spacing_file()` reads files as UTF-8 by default (new keyword-only `encoding` parameter) instead of the locale encoding
- The CLI reads stdin only when no argument is given; an explicit argument wins over piped stdin, and an explicit `-` argument always means stdin
- CLI usage errors exit 2 (argparse convention)
- Requires Python >= 3.11

New:

- HTML tag protection (attribute values still spaced), tag mentions, backtick protection, compound words, file paths, per-line slash/pipe/plus readings, affix readings
- `pangu.has_proper_spacing(text)`
- CLI `-c/--check`: exit 0 if the text has proper spacing, 1 if not (corrected text on stderr)

Internal:

- Packaging moved to `pyproject.toml` + `uv_build`; `src/pangu/` package layout replaces the single-file module
- The engine (`pangu._core`) deliberately mirrors pangu.js `src/shared/index.ts` so upstream releases port as a mechanical diff (see `docs/adr/0001`)

## v4.0.6.1 / 2019-02-09

- Implement **Paranoid Text Spacing Algorithm v4**
- Support Python 3.7
- Drop Python 2.7 support

## v3.3.0.1 / 2018-01-20

- Support Python 3.6
- Add a method: `pangu.spacing_file()`
- Add a command-line tool: `pangu`

## v3.0.0 / 2016-01-24

- Support Python 3.5
- Refactoring
- Rename `text_spacing()` to `spacing_text()`

## v2.5.6.3 / 2015-05-18

- Add an alias to `spacing()`: `text_spacing()`
- Fix unicode issue in Python 2.x

## v2.5.6.2 / 2015-05-17

- Fix setup.py

## v2.5.6 / 2015-05-17

- Implement **Paranoid Text Spacing Algorithm v2**
- Synchronize version number with [pangu.js](https://github.com/vinta/pangu.js)

## v1.0.0 / 2014-02-12

- Hello World
