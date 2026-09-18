from pangu import space_text


# \u2026
def test_handle_symbol():
    assert space_text("前面…後面") == "前面… 後面"
    assert space_text("前面……後面") == "前面…… 後面"
