import io
import subprocess
import sys

import pytest

from pangu import __version__, cli


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
    # the stdin behavior note lives in the help epilog, not the README
    assert "argument wins over piped stdin" in output


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
    # self-identifying so users can tell pangu.py from pangu.js when both are installed
    assert capsys.readouterr().out.strip() == f"pangu.py {__version__}"


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


# Stdin behavior, same rules as the pangu.js CLI since its v9.1
def test_stdin_is_used_when_no_argument(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", io.StringIO("中文abc"))
    assert cli([]) == 0
    assert capsys.readouterr().out == "中文 abc\n"


def test_stdin_composes_with_text_flag(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", io.StringIO("測試CLI參數\n"))
    assert cli(["-t"]) == 0
    assert capsys.readouterr().out == "測試 CLI 參數\n"


def test_dash_argument_always_means_stdin(monkeypatch, capsys):
    monkeypatch.setattr(sys, "stdin", io.StringIO("老婆餅裡面沒有老婆\n"))
    assert cli(["-"]) == 0
    assert capsys.readouterr().out == "老婆餅裡面沒有老婆\n"


def test_preserve_line_structure_of_multiline_stdin(monkeypatch, capsys):
    # print() restores the one trailing newline that reading stdin dropped, so piped input passes through byte for byte
    monkeypatch.setattr(sys, "stdin", io.StringIO("第一行有bug\n第二行有Java\n"))
    assert cli([]) == 0
    assert capsys.readouterr().out == "第一行有 bug\n第二行有 Java\n"


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


def test_file_mode_dash_reads_stdin(monkeypatch, capsys):
    # -f - is the conventional spelling for "the file is stdin" (cf. tar -f -)
    monkeypatch.setattr(sys, "stdin", io.StringIO("老婆餅裡面沒有老婆，JavaScript裡面也沒有Java\n"))
    assert cli(["-f", "-"]) == 0
    assert capsys.readouterr().out == "老婆餅裡面沒有老婆，JavaScript 裡面也沒有 Java\n"


def test_reject_file_flag_without_path_even_when_piped(monkeypatch, capsys):
    # a missing path is a usage error instead of a stdin fallback
    monkeypatch.setattr(sys, "stdin", io.StringIO("/some/path.txt"))
    with pytest.raises(SystemExit) as excinfo:
        cli(["-f"])
    assert excinfo.value.code == 2
    assert "argument --file: expected a file path" in capsys.readouterr().err


def test_reject_file_flag_with_empty_path_without_crashing(monkeypatch, capsys):
    # an empty string is what -f "$EMPTY_VAR" expands to: a missing path, not a file to open
    monkeypatch.setattr(sys, "stdin", io.StringIO("中文abc"))
    with pytest.raises(SystemExit) as excinfo:
        cli(["-f", ""])
    assert excinfo.value.code == 2
    err = capsys.readouterr().err
    assert "argument --file: expected a file path" in err
    assert "Traceback" not in err


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
