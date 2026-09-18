from pangu import space_text


def test_handle_symbol():
    assert space_text("前面;後面") == "前面; 後面"

    # DO NOT change if already spacing
    assert space_text("前面 ; 後面") == "前面 ; 後面"
    assert space_text("前面; 後面") == "前面; 後面"

    # Rare cases, ignore
    # assert space_text("前面 ;後面") == "前面 ;後面"
