from pangu import spacing_text


# Symbol ? only add space on the right
def test_handle_symbol():
    assert spacing_text("前面?") == "前面?"
    assert spacing_text("前面??") == "前面??"
    assert spacing_text("前面???") == "前面???"
    assert spacing_text("前面?後面") == "前面? 後面"
    assert spacing_text("前面??後面") == "前面?? 後面"
    assert spacing_text("前面???後面") == "前面??? 後面"
    assert spacing_text("前面?abc") == "前面? abc"
    assert spacing_text("前面?123") == "前面? 123"
    assert spacing_text("所以,請問Jackey的鼻子有幾個?3.14個") == "所以, 請問 Jackey 的鼻子有幾個? 3.14 個"

    # DO NOT change if already spacing
    assert spacing_text("前面 ? 後面") == "前面 ? 後面"
    assert spacing_text("前面? 後面") == "前面? 後面"
    # assert spacing_text("前面 ?後面") == "前面 ?後面"  # Rare cases (basically a typo), ignore
