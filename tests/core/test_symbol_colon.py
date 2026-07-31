from pangu import spacing_text


# When the symbol appears only 1 time in one line
def test_handle_symbol_as_colon_only_add_space_on_the_right():
    assert spacing_text("前面:後面") == "前面: 後面"

    # DO NOT change if already spacing
    assert spacing_text("前面 : 後面") == "前面 : 後面"
    assert spacing_text("前面: 後面") == "前面: 後面"
    assert spacing_text("前面 :後面") == "前面 :後面"

    # Special cases
    assert spacing_text("電話:123456789") == "電話: 123456789"
    assert spacing_text("前面:I have no idea後面") == "前面: I have no idea 後面"
    assert spacing_text("前面: I have no idea後面") == "前面: I have no idea 後面"

    # FIXME
    # assert spacing_text("前面:)後面") == "前面 :) 後面"


# When the symbol appears 2+ times or more in one line
def test_handle_symbol_as_separator():
    # FIXME
    # assert spacing_text("前面:後面:再後面") == "前面:後面:再後面"
    # assert spacing_text("前面:後面:再後面:更後面") == "前面:後面:再後面:更後面"
    # assert spacing_text("前面:後面:再後面:更後面:超後面") == "前面:後面:再後面:更後面:超後面"
    pass
