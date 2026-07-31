from pangu import spacing_text


# Symbol ! only add space on the right
def test_handle_symbol():
    assert spacing_text("前面!") == "前面!"
    assert spacing_text("前面!!") == "前面!!"
    assert spacing_text("前面!!!") == "前面!!!"
    assert spacing_text("前面!後面") == "前面! 後面"
    assert spacing_text("前面!!後面") == "前面!! 後面"
    assert spacing_text("前面!!!後面") == "前面!!! 後面"
    assert spacing_text("前面!abc") == "前面! abc"
    assert spacing_text("前面!123") == "前面! 123"
    assert spacing_text("前面2!的階乘") == "前面 2! 的階乘"

    assert spacing_text("你還在用Yahoo!奇摩？") == "你還在用 Yahoo! 奇摩？"

    # DO NOT change if already spacing
    assert spacing_text("前面 ! 後面") == "前面 ! 後面"
    assert spacing_text("前面! 後面") == "前面! 後面"
    # assert spacing_text("前面 !後面") == "前面 !後面"  # Rare cases (basically a typo), ignore
