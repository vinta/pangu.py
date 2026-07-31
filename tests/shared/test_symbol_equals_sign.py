from pangu import spacing_text


# When CJK touches the = directly
def test_handle_symbol_as_operator():
    assert spacing_text("前面=後面") == "前面 = 後面"
    assert spacing_text("Vinta=陳上進") == "Vinta = 陳上進"
    assert spacing_text("陳上進=Vinta") == "陳上進 = Vinta"

    # DO NOT change if already spacing
    assert spacing_text("前面 = 後面") == "前面 = 後面"
    assert spacing_text("Vinta = Mollie") == "Vinta = Mollie"
    assert spacing_text("Vinta = 陳上進") == "Vinta = 陳上進"
    assert spacing_text("陳上進 = Vinta") == "陳上進 = Vinta"
    assert spacing_text("得到一個 A = B 的結果") == "得到一個 A = B 的結果"


# An equals sign with half-width characters on both sides binds them into one token,
# spaced from CJK as a unit and never split
def test_handle_symbol_as_equals_token():
    assert spacing_text("Vinta=Mollie") == "Vinta=Mollie"  # If no CJK, DO NOT change
    assert spacing_text("得到一個A=B的結果") == "得到一個 A=B 的結果"
    assert spacing_text("設定a=1之後執行") == "設定 a=1 之後執行"
    assert spacing_text("網址是example.com?foo=bar&baz=1的頁面") == "網址是 example.com?foo=bar&baz=1 的頁面"


def test_handle_symbol_as_special_case():
    assert spacing_text("用=>寫箭頭函式") == "用 => 寫箭頭函式"
