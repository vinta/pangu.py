from pangu import space_text


def test_handle_symbol_as_separator():
    assert space_text("前面_後面") == "前面_後面"
    assert space_text("Vinta_Abc123") == "Vinta_Abc123"
    assert space_text("Vinta_Abc123_Kitten") == "Vinta_Abc123_Kitten"
    assert space_text("Vinta_貓咪") == "Vinta_貓咪"
    assert space_text("貓咪_Vinta") == "貓咪_Vinta"
    assert space_text("陳上進_貓咪_Abc123") == "陳上進_貓咪_Abc123"
    assert space_text("陳上進_Abc123_貓咪") == "陳上進_Abc123_貓咪"
    assert space_text("Abc123_Vinta_貓咪") == "Abc123_Vinta_貓咪"
    assert space_text("Abc123_陳上進_貓咪") == "Abc123_陳上進_貓咪"
    assert space_text("得到一個A_B的結果") == "得到一個 A_B 的結果"

    assert space_text("為什麼你們就是不能加個空格呢？_20771210_最終版_v365.7.24.zip") == "為什麼你們就是不能加個空格呢？_20771210_最終版_v365.7.24.zip"

    # Rare cases, ignore
    # assert space_text("前面 _ 後面") == "前面 _ 後面"
    # assert space_text("Vinta _ Abc123") == "Vinta _ Abc123"
    # assert space_text("Vinta _ Abc123 _ Kitten") == "Vinta _ Abc123 _ Kitten"
    # assert space_text("陳上進 _ 貓咪 _ Abc123") == "陳上進 _ 貓咪 _ Abc123"
    # assert space_text("陳上進 _ Abc123 _ 貓咪") == "陳上進 _ Abc123 _ 貓咪"
    # assert space_text("Abc123 _ Vinta _ 貓咪") == "Abc123 _ Vinta _ 貓咪"
    # assert space_text("Abc123 _ 陳上進 _ 貓咪") == "Abc123 _ 陳上進 _ 貓咪"
