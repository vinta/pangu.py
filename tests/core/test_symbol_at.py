from pangu import space_text


def test_handle_symbol_as_at():
    assert space_text("前面@vinta後面") == "前面 @vinta 後面"
    assert space_text("前面@vinta_chen後面") == "前面 @vinta_chen 後面"
    assert space_text("前面@VintaChen後面") == "前面 @VintaChen 後面"
    assert space_text("前面@陳上進 後面") == "前面 @陳上進 後面"
