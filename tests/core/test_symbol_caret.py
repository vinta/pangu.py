from pangu import space_text


# When the symbol appears only 1 time or shows up with other operators in one line
def test_handle_symbol_as_operator_always_spacing():
    assert space_text("前面^後面") == "前面 ^ 後面"
    assert space_text("前面 ^ 後面") == "前面 ^ 後面"
