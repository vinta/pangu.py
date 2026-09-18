from pangu import space_text


def test_handle_symbol():
    assert space_text("前面?") == "前面?"
    assert space_text("前面??") == "前面??"
    assert space_text("前面???") == "前面???"
    assert space_text("前面?後面") == "前面? 後面"
    assert space_text("前面??後面") == "前面?? 後面"
    assert space_text("前面???後面") == "前面??? 後面"
    assert space_text("前面?abc") == "前面? abc"
    assert space_text("前面?123") == "前面? 123"
    assert space_text("所以,請問Jackey的鼻子有幾個?3.14個") == "所以, 請問 Jackey 的鼻子有幾個? 3.14 個"

    # DO NOT change if already spacing
    assert space_text("前面 ? 後面") == "前面 ? 後面"
    assert space_text("前面? 後面") == "前面? 後面"

    # Rare cases, ignore
    # assert space_text("前面 ?後面") == "前面 ?後面"
