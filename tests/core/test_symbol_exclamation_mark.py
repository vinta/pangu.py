from pangu import space_text


def test_handle_symbol():
    assert space_text("前面!") == "前面!"
    assert space_text("前面!!") == "前面!!"
    assert space_text("前面!!!") == "前面!!!"
    assert space_text("前面!後面") == "前面! 後面"
    assert space_text("前面!!後面") == "前面!! 後面"
    assert space_text("前面!!!後面") == "前面!!! 後面"
    assert space_text("前面!abc") == "前面! abc"
    assert space_text("前面!123") == "前面! 123"
    assert space_text("前面2!的階乘") == "前面 2! 的階乘"

    assert space_text("你還在用Yahoo!奇摩？") == "你還在用 Yahoo! 奇摩？"

    assert space_text('! git commit -a -m "蛤"') == '! git commit -a -m "蛤"'

    # DO NOT change if already spacing
    assert space_text("前面 ! 後面") == "前面 ! 後面"
    assert space_text("前面! 後面") == "前面! 後面"

    # Rare cases, ignore
    # assert space_text("前面 !後面") == "前面 !後面"
