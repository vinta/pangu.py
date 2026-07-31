import io
import subprocess
import sys
from pathlib import Path

import pytest

from pangu import __version__, cli

FIXTURES = Path(__file__).parent.parent / "fixtures"


class _TtyStringIO(io.StringIO):
    def isatty(self):
        return True


# Ported from pangu.js tests/node/cli.test.ts
def test_handle_help_message_display(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli(["--help"])
    assert excinfo.value.code == 0
    output = capsys.readouterr().out
    assert "usage: pangu" in output
    assert "Paranoid text spacing" in output


def test_handle_text_from_command_line(capsys):
    assert cli(["-t", "你從什麼時候開始產生了我沒使用Monkey Patch的錯覺？"]) == 0
    assert capsys.readouterr().out.strip() == "你從什麼時候開始產生了我沒使用 Monkey Patch 的錯覺？"


def test_handle_file_content(tmp_path, capsys):
    temp_file = tmp_path / "temp_test.txt"
    temp_file.write_text("老婆餅裡面沒有老婆，JavaScript裡面也沒有Java", encoding="utf-8")
    assert cli(["-f", str(temp_file)]) == 0
    assert capsys.readouterr().out.strip() == "老婆餅裡面沒有老婆，JavaScript 裡面也沒有 Java"


def test_handle_text_by_default(capsys):
    assert cli(["中文abc"]) == 0
    assert capsys.readouterr().out.strip() == "中文 abc"


def test_handle_version(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cli(["--version"])
    assert excinfo.value.code == 0
    assert capsys.readouterr().out.strip() == __version__


def test_check_proper_spacing_exits_zero(capsys):
    assert cli(["-c", "中文 abc"]) == 0
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""


def test_check_improper_spacing_exits_one_with_corrected_on_stderr(capsys):
    assert cli(["-c", "中文abc"]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "Corrected: 中文 abc\n"


# Python-only stdin behavior
def test_stdin_is_used_when_no_argument(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", io.StringIO("中文abc"))
    assert cli([]) == 0
    assert capsys.readouterr().out == "中文 abc\n"


def test_argument_wins_over_piped_stdin(monkeypatch, capsys):
    # v5 behavior change from v4 (stdin used to win): the rule pangu.js#309 adopts
    monkeypatch.setattr(sys, "stdin", io.StringIO("stdin中文abc"))
    assert cli(["-t", "引數中文abc"]) == 0
    assert capsys.readouterr().out == "引數中文 abc\n"


def test_check_composes_with_stdin(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", io.StringIO("中文abc"))
    assert cli(["-c"]) == 1
    assert capsys.readouterr().err == "Corrected: 中文 abc\n"

    monkeypatch.setattr(sys, "stdin", io.StringIO("中文 abc"))
    assert cli(["-c"]) == 0


def test_file_mode_requires_explicit_path(monkeypatch, capsys):
    # stdin only ever carries text, never a file path
    monkeypatch.setattr(sys, "stdin", io.StringIO("/some/path.txt"))
    with pytest.raises(SystemExit) as excinfo:
        cli(["-f"])
    assert excinfo.value.code == 2
    assert "requires a file path" in capsys.readouterr().err


def test_no_input_on_a_tty_is_a_usage_error(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", _TtyStringIO())
    with pytest.raises(SystemExit) as excinfo:
        cli([])
    assert excinfo.value.code == 2
    assert "usage: pangu" in capsys.readouterr().err


def test_mutually_exclusive_modes_are_a_usage_error():
    with pytest.raises(SystemExit) as excinfo:
        cli(["-t", "-f", "x"])
    assert excinfo.value.code == 2


def test_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        cli(["-f", str(tmp_path / "no-such-file.txt")])


def test_broken_pipe_does_not_stack_trace(tmp_path):
    # `pangu -f big.txt | head` must not stack-trace: force a real SIGPIPE with
    # output far larger than the OS pipe buffer
    big_file = tmp_path / "big.txt"
    big_file.write_text("中文abc\n" * 100_000, encoding="utf-8")
    script = f'"{sys.executable}" -m pangu -f "{big_file}" | head -c 8'
    result = subprocess.run(["sh", "-c", script], capture_output=True, text=True, check=False)
    assert result.returncode == 0
    assert "Traceback" not in result.stderr
