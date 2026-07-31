from pangu import spacing_text


def test_handle_symbol():
    assert spacing_text("前面\\後面") == "前面 \\ 後面"
    assert spacing_text("前面 \\ 後面") == "前面 \\ 後面"


def test_handle_symbol_as_escape_character():
    assert spacing_text("\\n") == "\\n"
    assert spacing_text("\\t") == "\\t"


def test_handle_symbol_as_windows_file_path():
    assert spacing_text("檔案在C:\\Users\\name\\") == "檔案在 C:\\Users\\name\\"
    assert spacing_text("程式在D:\\Program Files\\") == "程式在 D:\\Program Files\\"
    assert spacing_text("在C:\\Windows\\System32") == "在 C:\\Windows\\System32"
