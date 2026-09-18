from pangu import space_text


# When CJK touches the & directly
def test_handle_symbol_as_operator():
    assert space_text("前面&後面") == "前面 & 後面"
    assert space_text("Vinta&陳上進") == "Vinta & 陳上進"
    assert space_text("陳上進&Vinta") == "陳上進 & Vinta"

    # DO NOT change if already spacing
    assert space_text("前面 & 後面") == "前面 & 後面"
    assert space_text("Vinta & Mollie") == "Vinta & Mollie"
    assert space_text("Vinta & 陳上進") == "Vinta & 陳上進"
    assert space_text("陳上進 & Vinta") == "陳上進 & Vinta"
    assert space_text("得到一個 A & B 的結果") == "得到一個 A & B 的結果"


# An ampersand with half-width characters on both sides binds them into one token,
# spaced from CJK as a unit and never split. The & itself is untouched for the same
# reason "Vinta&Mollie" is: no CJK touches it - but CJK boundaries elsewhere still space
def test_handle_symbol_as_ampersand_token():
    assert space_text("Vinta&Mollie") == "Vinta&Mollie"  # If no CJK, DO NOT change
    assert space_text("得到一個A&B的結果") == "得到一個 A&B 的結果"
    assert space_text("本週S&P 500及Nasdaq同時下跌") == "本週 S&P 500 及 Nasdaq 同時下跌"
    assert space_text("接下來是Q&A時間") == "接下來是 Q&A 時間"
