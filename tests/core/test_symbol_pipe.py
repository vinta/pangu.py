from pangu import space_text


def test_handle_symbol_as_separator():
    assert space_text("前面|後面") == "前面 | 後面"
    assert space_text("Vinta|貓咪") == "Vinta | 貓咪"
    assert space_text("貓咪|Vinta") == "貓咪 | Vinta"
    assert space_text("陳上進|貓咪|Abc123") == "陳上進 | 貓咪 | Abc123"
    assert space_text("陳上進|Abc123|貓咪") == "陳上進 | Abc123 | 貓咪"
    assert space_text("Abc123|Vinta|貓咪") == "Abc123 | Vinta | 貓咪"
    assert space_text("Abc123|陳上進|貓咪") == "Abc123 | 陳上進 | 貓咪"
    assert space_text("作詞|林夕") == "作詞 | 林夕"
    assert space_text("文|張三 圖|李四") == "文 | 張三 圖 | 李四"
    assert space_text("支援的 Apple TV 型號|Disney+ 幫助中心|TW") == "支援的 Apple TV 型號 | Disney+ 幫助中心 | TW"

    # DO NOT change if already spacing
    assert space_text("前面 | 後面") == "前面 | 後面"
    assert space_text("Vinta | Abc123") == "Vinta | Abc123"
    assert space_text("Vinta | Abc123 | Kitten") == "Vinta | Abc123 | Kitten"
    assert space_text("陳上進 | 貓咪 | Abc123") == "陳上進 | 貓咪 | Abc123"
    assert space_text("陳上進 | Abc123 | 貓咪") == "陳上進 | Abc123 | 貓咪"
    assert space_text("Abc123 | Vinta | 貓咪") == "Abc123 | Vinta | 貓咪"
    assert space_text("Abc123 | 陳上進 | 貓咪") == "Abc123 | 陳上進 | 貓咪"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta|Abc123") == "Vinta|Abc123"  # If no CJK, DO NOT change
    assert space_text("Vinta|Abc123|Kitten") == "Vinta|Abc123|Kitten"
    assert space_text("ps aux|grep node") == "ps aux|grep node"
    assert space_text("條件是x|y的情況") == "條件是 x|y 的情況"
    assert space_text("得到一個A|B的結果") == "得到一個 A|B 的結果"
    assert space_text("得到一個A||B的結果") == "得到一個 A||B 的結果"
