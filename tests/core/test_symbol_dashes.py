from pangu import spacing_text


# — An em-dash is not a spaced half-width symbol, so it stays flush against CJK
def test_handle_em_dash_does_not_add_space_with_cjk():
    assert spacing_text("前面—後面") == "前面—後面"
    assert spacing_text("他說——不對") == "他說——不對"
