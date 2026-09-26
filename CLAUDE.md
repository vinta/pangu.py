# CLAUDE.md

## Project Overview

`pangu.py` is a text spacing library that automatically inserts whitespace between CJK (Chinese, Japanese, Korean) characters and half-width characters (alphabetical letters, numerical digits, and symbols). It is a Python port of the pangu.js v10 engine, shipped as a zero-dependency PyPI package with a module API and a CLI.

## Common Development Commands

```bash
make install                    # uv sync --locked + uv audit
make test                       # Run all tests (pytest)
make lint                       # ruff format --check + ruff check
make format                     # Auto-format and fix lint issues
make typecheck                  # ty check

uv run pytest tests/core/test_symbol_slash.py -v        # Run a single test file
uv run pytest -k "test_name" -v                         # Run tests matching a name
```

## Where Things Live

- Spacing engine, a 1:1 port of pangu.js `src/shared/index.ts`: `src/pangu/_core.py`
- Module API and CLI: `src/pangu/`
- Parity spec, ported 1:1 from pangu.js `tests/shared/`: `tests/core/`
- CLI and packaging tests: `tests/cli/`, `tests/test_package.py` (text fixtures in `fixtures/`)
- Domain language and algorithm semantics: `CONTEXT.md`; decision records: `docs/adr/`

## Gotchas

- Spacing rule changes flow downstream from pangu.js: fix or tweak rules upstream first, then port the diff. Read `CONTEXT.md` before touching `_core.py`, and keep it in sync when porting. Ported through pangu.js `8cd3a97d`: list pending upstream changes with `git -C ../pangu.js log 8cd3a97d.. -- src/shared src/node tests/shared tests/node`, and bump the hash after each sync.
- `_core.py` stays js-shaped on purpose: same UPPER_SNAKE pattern names, same pipeline order, regexes copied verbatim from pangu.js. Python's `re` supports the lookarounds pangu.js relies on (only variable-length lookbehind is missing, checked in code by the `_sub_*` helpers), so each upstream change ports as a line-for-line diff. Don't pythonize or "clean it up": idiomatic internals turn every sync into re-deriving the rules, the cost pangu.go pays because Go's RE2 has no lookarounds (ADR 0001).
- When porting a js regex, keep js `$` as `$` only if the input can never end in `\n`; otherwise use `\Z` (see `BRACKET_INNER_SPACES`). Python's `$` also matches before a trailing newline, js's does not. Avoid `\z`: it needs Python 3.14, above our `requires-python` floor.
- Commented-out asserts, FIXME comments, and `xfail(strict=True)` markers in `tests/core/` are intentional 1:1 ports of upstream FIXME cases and `it.fails` — leave them. The per-file test lint ignores in `pyproject.toml` exist for the same reason; don't widen them casually.
- The version lives in two places: `pyproject.toml` and `__version__` in `src/pangu/__init__.py`. `tests/test_package.py` fails CI if they drift.
- Write code comments in English with ASCII characters only. Never paste CJK sample text into a comment; describe the shape generically (`CJK | CJK`, `A+CJK`) and use `\uXXXX` escape notation when a specific character matters.

## External Tool Documentation

Pre-resolved Context7 IDs for the `find-docs` skill. Pass them to `ctx7 docs` and skip `ctx7 library`:

| Tool   | `libraryId`          |
| ------ | -------------------- |
| uv     | `/astral-sh/uv`      |
| ruff   | `/astral-sh/ruff`    |
| ty     | `/astral-sh/ty`      |
| pytest | `/pytest-dev/pytest` |
