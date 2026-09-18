from pangu import space_text


def test_handle_symbol_as_separator_do_not_spacing():
    assert space_text("前面_後面") == "前面_後面"
    assert space_text("Vinta_Mollie") == "Vinta_Mollie"
    assert space_text("Vinta_Mollie_Kitten") == "Vinta_Mollie_Kitten"
    assert space_text("Mollie_陳上進") == "Mollie_陳上進"
    assert space_text("陳上進_Mollie") == "陳上進_Mollie"
    assert space_text("陳上進_貓咪_Mollie") == "陳上進_貓咪_Mollie"
    assert space_text("陳上進_Mollie_貓咪") == "陳上進_Mollie_貓咪"
    assert space_text("Mollie_Vinta_貓咪") == "Mollie_Vinta_貓咪"
    assert space_text("Mollie_陳上進_貓咪") == "Mollie_陳上進_貓咪"
    assert space_text("得到一個A_B的結果") == "得到一個 A_B 的結果"

    assert space_text("為什麼你們就是不能加個空格呢？_20771210_最終版_v365.7.24.zip") == "為什麼你們就是不能加個空格呢？_20771210_最終版_v365.7.24.zip"

    # Rare cases, ignore
    # assert space_text("前面 _ 後面") == "前面 _ 後面"
    # assert space_text("Vinta _ Mollie") == "Vinta _ Mollie"
    # assert space_text("Vinta _ Mollie _ Kitten") == "Vinta _ Mollie _ Kitten"
    # assert space_text("陳上進 _ 貓咪 _ Mollie") == "陳上進 _ 貓咪 _ Mollie"
    # assert space_text("陳上進 _ Mollie _ 貓咪") == "陳上進 _ Mollie _ 貓咪"
    # assert space_text("Mollie _ Vinta _ 貓咪") == "Mollie _ Vinta _ 貓咪"
    # assert space_text("Mollie _ 陳上進 _ 貓咪") == "Mollie _ 陳上進 _ 貓咪"
