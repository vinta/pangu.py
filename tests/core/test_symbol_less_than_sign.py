from pangu import space_text


# When CJK touches the < directly
def test_handle_symbol_as_operator():
    assert space_text("前面<後面") == "前面 < 後面"
    assert space_text("Vinta<陳上進") == "Vinta < 陳上進"
    assert space_text("陳上進<Vinta") == "陳上進 < Vinta"

    # DO NOT change if already spacing
    assert space_text("前面 < 後面") == "前面 < 後面"
    assert space_text("Vinta < Mollie") == "Vinta < Mollie"
    assert space_text("Vinta < 陳上進") == "Vinta < 陳上進"
    assert space_text("陳上進 < Vinta") == "陳上進 < Vinta"
    assert space_text("得到一個 A < B 的結果") == "得到一個 A < B 的結果"


# A less-than sign with half-width characters on both sides binds them into one token,
# spaced from CJK as a unit and never split
def test_handle_symbol_as_less_than_token():
    assert space_text("Vinta<Mollie") == "Vinta<Mollie"  # If no CJK, DO NOT change
    assert space_text("得到一個A<B的結果") == "得到一個 A<B 的結果"
    assert space_text("如果A<B就繼續") == "如果 A<B 就繼續"
    assert space_text("條件是1<2的情況") == "條件是 1<2 的情況"
