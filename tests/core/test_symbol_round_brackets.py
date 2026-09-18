from pangu import space_text


def test_handle_symbols_as_round_brackets():
    assert space_text("前面(中文123漢字)後面") == "前面 (中文 123 漢字) 後面"
    assert space_text("前面(中文123)後面") == "前面 (中文 123) 後面"
    assert space_text("前面(123漢字)後面") == "前面 (123 漢字) 後面"
    assert space_text("前面(中文123) tail") == "前面 (中文 123) tail"
    assert space_text("head (中文123漢字)後面") == "head (中文 123 漢字) 後面"
    assert space_text("head (中文123漢字) tail") == "head (中文 123 漢字) tail"
    assert space_text('(or simply "React")') == '(or simply "React")'
    assert space_text("function(123)") == "function(123)"
    assert space_text("我看过的电影(1404)") == "我看过的电影 (1404)"

    assert space_text("預定於繳款截止日114/07/02(遇假日順延)之次一營業日進行扣款") == "預定於繳款截止日 114/07/02 (遇假日順延) 之次一營業日進行扣款"

    assert space_text("OperationalError: (2006, 'MySQL server has gone away')") == "OperationalError: (2006, 'MySQL server has gone away')"

    assert space_text("Chang Stream(变更记录流)是指collection(数据库集合)的变更事件流") == "Chang Stream (变更记录流) 是指 collection (数据库集合) 的变更事件流"


def test_handle_multiline_content_in_round_brackets():
    # A space before a newline is mid-content, not a bracket-edge space: only the literal string edges get stripped
    assert space_text("(x \n)中") == "(x \n) 中"
    assert space_text("(參數 \n)後面") == "(參數 \n) 後面"
