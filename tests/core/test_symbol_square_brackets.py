from pangu import spacing_text


def test_handle_symbols_as_square_brackets():
    assert spacing_text("前面[中文123漢字]後面") == "前面 [中文 123 漢字] 後面"
    assert spacing_text("前面[中文123]後面") == "前面 [中文 123] 後面"
    assert spacing_text("前面[123漢字]後面") == "前面 [123 漢字] 後面"
    assert spacing_text("前面[中文123] tail") == "前面 [中文 123] tail"
    assert spacing_text("head [中文123漢字]後面") == "head [中文 123 漢字] 後面"
    assert spacing_text("head [中文123漢字] tail") == "head [中文 123 漢字] tail"


def test_handle_multiline_content_in_square_brackets():
    # A space before a newline is mid-content, not a bracket-edge space: only the literal string edges get stripped
    assert spacing_text("[x \n]中") == "[x \n] 中"
    assert spacing_text("中[ 多行\n內容 ]") == "中 [多行\n內容]"
