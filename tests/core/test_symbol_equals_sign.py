from pangu import space_text


def test_handle_symbol_as_operator():
    assert space_text("前面=後面") == "前面 = 後面"
    assert space_text("Vinta=陳上進") == "Vinta = 陳上進"
    assert space_text("陳上進=Vinta") == "陳上進 = Vinta"

    # DO NOT change if already spacing
    assert space_text("前面 = 後面") == "前面 = 後面"
    assert space_text("Vinta = Abc123") == "Vinta = Abc123"
    assert space_text("Vinta = 陳上進") == "Vinta = 陳上進"
    assert space_text("陳上進 = Vinta") == "陳上進 = Vinta"
    assert space_text("得到一個 A = B 的結果") == "得到一個 A = B 的結果"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta=Abc123") == "Vinta=Abc123"  # If no CJK, DO NOT change
    assert space_text("得到一個A=B的結果") == "得到一個 A=B 的結果"
    assert space_text("設定a=1之後執行") == "設定 a=1 之後執行"
    assert space_text("網址是example.com?foo=bar&baz=1的頁面") == "網址是 example.com?foo=bar&baz=1 的頁面"


def test_handle_symbol_as_preserved_pattern():
    assert space_text("用=>寫箭頭函式") == "用 => 寫箭頭函式"
