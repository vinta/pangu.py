from pangu import space_text


def test_handle_superscript_as_suffix():
    assert space_text("前面E=mc²後面") == "前面 E=mc² 後面"

    assert space_text("115年賽事加碼：7/21-10/8 新申請MOD+自選餐(全選)/影劇館⁺加碼") == "115 年賽事加碼：7/21-10/8 新申請 MOD + 自選餐 (全選)/影劇館⁺ 加碼"

    assert space_text("甲⁰乙、甲¹乙、甲²乙、甲³乙、甲⁴乙、甲⁵乙、甲⁶乙、甲⁷乙、甲⁸乙、甲⁹乙") == "甲⁰ 乙、甲¹ 乙、甲² 乙、甲³ 乙、甲⁴ 乙、甲⁵ 乙、甲⁶ 乙、甲⁷ 乙、甲⁸ 乙、甲⁹ 乙"
    assert space_text("甲ⁱ乙、甲ⁿ乙、甲⁺乙、甲⁻乙、甲⁼乙") == "甲ⁱ 乙、甲ⁿ 乙、甲⁺ 乙、甲⁻ 乙、甲⁼ 乙"
    assert space_text("甲⁽註⁾乙") == "甲⁽註⁾ 乙"


# \u2122
def test_handle_symbol():
    assert space_text("Trademark™後面") == "Trademark™ 後面"
    assert space_text("商標™後面") == "商標™ 後面"


# \u2120
def test_handle_symbol_2():
    assert space_text("Service Mark℠後面") == "Service Mark℠ 後面"
    assert space_text("服務商標℠後面") == "服務商標℠ 後面"


# \u00ae
def test_handle_symbol_3():
    assert space_text("Registered Trademark®後面") == "Registered Trademark® 後面"
    assert space_text("註冊商標®公司") == "註冊商標® 公司"
    assert space_text("註冊商標®與Trademark™") == "註冊商標® 與 Trademark™"


# \u00a9
def test_handle_symbol_4():
    assert space_text("版權所有©2026東亞重工") == "版權所有 © 2026 東亞重工"
    assert space_text("版權所有©2012-2026東亞重工") == "版權所有 © 2012-2026 東亞重工"
    assert space_text("Copyright © 2026東亞重工") == "Copyright © 2026 東亞重工"
    assert space_text("Copyright © 2012-2026東亞重工") == "Copyright © 2012-2026 東亞重工"
