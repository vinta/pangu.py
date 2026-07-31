from pangu import spacing_text


# Symbol , only add space on the right
def test_handle_symbol():
    assert spacing_text("前面,後面") == "前面, 後面"

    assert spacing_text('"你好",她說') == '"你好", 她說'
    assert spacing_text("每月只要1,000元") == "每月只要 1,000 元"
    assert spacing_text("精采5G購機方案(30個月),月繳599元購機優惠(30個月)") == "精采 5G 購機方案 (30 個月), 月繳 599 元購機優惠 (30 個月)"

    # DO NOT change if already spacing
    assert spacing_text("前面 , 後面") == "前面 , 後面"
    assert spacing_text("前面, 後面") == "前面, 後面"
    # assert spacing_text("前面 ,後面") == "前面 ,後面"  # Rare cases (basically a typo), ignore
