from pangu import space_text


# Symbol @ only add space on the left
def test_handle_symbol_as_at():
    assert space_text("請@vinta吃大便") == "請 @vinta 吃大便"
    assert space_text("請@vinta_chen吃大便") == "請 @vinta_chen 吃大便"
    assert space_text("請@VintaChen吃大便") == "請 @VintaChen 吃大便"
    assert space_text("請@陳上進 吃大便") == "請 @陳上進 吃大便"
