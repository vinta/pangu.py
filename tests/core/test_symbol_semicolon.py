from pangu import spacing_text


# Symbol ; only add space on the right
def test_handle_symbol():
    assert spacing_text("前面;後面") == "前面; 後面"

    # DO NOT change if already spacing
    assert spacing_text("前面 ; 後面") == "前面 ; 後面"
    assert spacing_text("前面; 後面") == "前面; 後面"
    # assert spacing_text("前面 ;後面") == "前面 ;後面"  # Rare cases (basically a typo), ignore
