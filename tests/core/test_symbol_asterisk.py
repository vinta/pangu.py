from pangu import spacing_text


# When CJK touches the * directly
def test_handle_symbol_as_operator():
    assert spacing_text("前面*後面") == "前面 * 後面"
    assert spacing_text("Vinta*陳上進") == "Vinta * 陳上進"
    assert spacing_text("陳上進*Vinta") == "陳上進 * Vinta"
    assert spacing_text("標示*的欄位代表必填") == "標示 * 的欄位代表必填"

    # DO NOT change if already spacing
    assert spacing_text("前面 * 後面") == "前面 * 後面"
    assert spacing_text("Vinta * Mollie") == "Vinta * Mollie"
    assert spacing_text("Vinta * 陳上進") == "Vinta * 陳上進"
    assert spacing_text("陳上進 * Vinta") == "陳上進 * Vinta"
    assert spacing_text("得到一個 A * B 的結果") == "得到一個 A * B 的結果"


# An asterisk with half-width characters on both sides binds them into one token,
# spaced from CJK as a unit and never split
def test_handle_symbol_as_asterisk_token():
    assert spacing_text("Vinta*Mollie") == "Vinta*Mollie"  # If no CJK, DO NOT change
    assert spacing_text("得到一個A*B的結果") == "得到一個 A*B 的結果"
    assert spacing_text("算式是2*3的積") == "算式是 2*3 的積"


def test_handle_symbol_as_special_case():
    assert spacing_text("刪掉*.log的檔案") == "刪掉 *.log 的檔案"
