from pangu import spacing_text


def test_handle_symbol():
    assert spacing_text("前面$後面") == "前面 $ 後面"
    assert spacing_text("前面 $ 後面") == "前面 $ 後面"
    assert spacing_text("前面$100後面") == "前面 $100 後面"
