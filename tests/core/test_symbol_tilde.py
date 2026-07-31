from pangu import spacing_text


# Symbol ~ only add space on the right
def test_handle_symbol():
    assert spacing_text("前面~") == "前面~"
    assert spacing_text("前面~~") == "前面~~"
    assert spacing_text("前面~~~") == "前面~~~"
    assert spacing_text("前面~後面") == "前面~ 後面"
    assert spacing_text("前面~~後面") == "前面~~ 後面"
    assert spacing_text("前面~~~後面") == "前面~~~ 後面"
    assert spacing_text("前面~abc") == "前面~ abc"
    assert spacing_text("前面~123") == "前面~ 123"

    # DO NOT change if already spacing
    assert spacing_text("前面 ~ 後面") == "前面 ~ 後面"
    assert spacing_text("前面~ 後面") == "前面~ 後面"
    assert spacing_text("前面 ~後面") == "前面 ~後面"

    # Special cases
    assert spacing_text("前面~=後面") == "前面 ~= 後面"
    assert spacing_text("前面 ~= 後面") == "前面 ~= 後面"
