from pangu import spacing_text


# A pipe in direct CJK contact makes every pipe on the line a separator,
# decided per line like slash reading
def test_handle_symbol_as_separator():
    assert spacing_text("前面|後面") == "前面 | 後面"
    assert spacing_text("Mollie|陳上進") == "Mollie | 陳上進"
    assert spacing_text("陳上進|Mollie") == "陳上進 | Mollie"
    assert spacing_text("陳上進|貓咪|Mollie") == "陳上進 | 貓咪 | Mollie"
    assert spacing_text("陳上進|Mollie|貓咪") == "陳上進 | Mollie | 貓咪"
    assert spacing_text("Mollie|Vinta|貓咪") == "Mollie | Vinta | 貓咪"
    assert spacing_text("Mollie|陳上進|貓咪") == "Mollie | 陳上進 | 貓咪"
    assert spacing_text("作詞|林夕") == "作詞 | 林夕"
    assert spacing_text("文|張三 圖|李四") == "文 | 張三 圖 | 李四"
    assert spacing_text("支援的 Apple TV 型號|Disney+ 幫助中心|TW") == "支援的 Apple TV 型號 | Disney+ 幫助中心 | TW"

    # DO NOT change if already spacing
    assert spacing_text("前面 | 後面") == "前面 | 後面"
    assert spacing_text("Vinta | Mollie") == "Vinta | Mollie"
    assert spacing_text("Vinta | Mollie | Kitten") == "Vinta | Mollie | Kitten"
    assert spacing_text("陳上進 | 貓咪 | Mollie") == "陳上進 | 貓咪 | Mollie"
    assert spacing_text("陳上進 | Mollie | 貓咪") == "陳上進 | Mollie | 貓咪"
    assert spacing_text("Mollie | Vinta | 貓咪") == "Mollie | Vinta | 貓咪"
    assert spacing_text("Mollie | 陳上進 | 貓咪") == "Mollie | 陳上進 | 貓咪"


# On a line where no pipe touches CJK, a pipe binds half-width characters
# into one token, spaced from CJK as a unit and never split
def test_handle_symbol_as_pipe_token():
    assert spacing_text("Vinta|Mollie") == "Vinta|Mollie"  # If no CJK, DO NOT change
    assert spacing_text("Vinta|Mollie|Kitten") == "Vinta|Mollie|Kitten"
    assert spacing_text("ps aux|grep node") == "ps aux|grep node"
    assert spacing_text("條件是x|y的情況") == "條件是 x|y 的情況"
    assert spacing_text("得到一個A|B的結果") == "得到一個 A|B 的結果"
    assert spacing_text("得到一個A||B的結果") == "得到一個 A||B 的結果"
