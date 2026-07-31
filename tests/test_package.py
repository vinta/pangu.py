import importlib.metadata
from pathlib import Path

import pytest

import pangu
from pangu import spacing_file

FIXTURES = Path(__file__).parent.parent / "fixtures"


def test_version_matches_package_metadata():
    # Guard against the static version in pyproject.toml and __init__.py drifting apart
    assert pangu.__version__ == importlib.metadata.version("pangu")


def test_console_script_names():
    scripts = {ep.name for ep in importlib.metadata.distribution("pangu").entry_points if ep.group == "console_scripts"}
    assert scripts == {"pangu", "pangu-py"}


# Ported from pangu.js tests/node/index.test.ts (spacingFileSync)
def test_spacing_file():
    expected = (FIXTURES / "text-file.expected.txt").read_text(encoding="utf-8")
    assert spacing_file(FIXTURES / "text-file.txt") == expected


def test_spacing_file_without_eof_newline():
    expected = (FIXTURES / "text-file-no-eof-newline.expected.txt").read_text(encoding="utf-8")
    assert spacing_file(FIXTURES / "text-file-no-eof-newline.txt") == expected


def test_spacing_file_accepts_str_path():
    assert spacing_file(str(FIXTURES / "test_file.txt")) == "老婆餅裡面沒有老婆，JavaScript 裡面也沒有 Java\n"


def test_spacing_file_encoding_keyword(tmp_path):
    path = tmp_path / "utf16.txt"
    path.write_text("中文abc", encoding="utf-16")
    assert spacing_file(path, encoding="utf-16") == "中文 abc"


def test_spacing_file_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        spacing_file(FIXTURES / "no-such-file.txt")


def test_spacing_file_wrong_encoding_raises(tmp_path):
    path = tmp_path / "utf16.txt"
    path.write_text("中文abc", encoding="utf-16")
    with pytest.raises(UnicodeDecodeError):
        spacing_file(path)
