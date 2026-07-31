from pangu import spacing_text


def test_handle_symbols_as_round_brackets():
    assert spacing_text("前面(中文123漢字)後面") == "前面 (中文 123 漢字) 後面"
    assert spacing_text("前面(中文123)後面") == "前面 (中文 123) 後面"
    assert spacing_text("前面(123漢字)後面") == "前面 (123 漢字) 後面"
    assert spacing_text("前面(中文123) tail") == "前面 (中文 123) tail"
    assert spacing_text("head (中文123漢字)後面") == "head (中文 123 漢字) 後面"
    assert spacing_text("head (中文123漢字) tail") == "head (中文 123 漢字) tail"
    assert spacing_text('(or simply "React")') == '(or simply "React")'
    assert spacing_text("function(123)") == "function(123)"
    assert spacing_text("我看过的电影(1404)") == "我看过的电影 (1404)"

    assert spacing_text("預定於繳款截止日114/07/02(遇假日順延)之次一營業日進行扣款") == "預定於繳款截止日 114/07/02 (遇假日順延) 之次一營業日進行扣款"

    assert spacing_text("OperationalError: (2006, 'MySQL server has gone away')") == "OperationalError: (2006, 'MySQL server has gone away')"

    assert spacing_text("Chang Stream(变更记录流)是指collection(数据库集合)的变更事件流") == "Chang Stream (变更记录流) 是指 collection (数据库集合) 的变更事件流"

    assert spacing_text("从结果来看，当a.b销毁后，`a.getB()`返回值为null") == "从结果来看，当 a.b 销毁后，`a.getB()` 返回值为 null"

    assert spacing_text("后续会直接用iframe window.addEventListener('message')") == "后续会直接用 iframe window.addEventListener('message')"
