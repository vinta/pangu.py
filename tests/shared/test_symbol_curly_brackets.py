from pangu import spacing_text


def test_handle_symbols_as_curly_brackets():
    assert spacing_text("前面{中文123漢字}後面") == "前面 {中文 123 漢字} 後面"
    assert spacing_text("前面{中文123}後面") == "前面 {中文 123} 後面"
    assert spacing_text("前面{123漢字}後面") == "前面 {123 漢字} 後面"
    assert spacing_text("前面{中文123} tail") == "前面 {中文 123} tail"
    assert spacing_text("head {中文123漢字}後面") == "head {中文 123 漢字} 後面"
    assert spacing_text("head {中文123漢字} tail") == "head {中文 123 漢字} tail"
