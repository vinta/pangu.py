from pangu import spacing_text


# \u2026
def test_handle_symbol_only_add_space_on_the_right():
    assert spacing_text("前面…後面") == "前面… 後面"
    assert spacing_text("前面……後面") == "前面…… 後面"
