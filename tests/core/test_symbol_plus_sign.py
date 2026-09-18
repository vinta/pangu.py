from pangu import space_text


# When CJK touches the + directly
def test_handle_symbol_as_operator():
    assert space_text("前面+後面") == "前面 + 後面"
    # assert space_text("Vinta+陳上進") == "Vinta + 陳上進"  # Rare cases, ignore
    assert space_text("陳上進+Vinta") == "陳上進 + Vinta"
    assert space_text("你+我=我們") == "你 + 我 = 我們"

    # CJK brand suffixes (公視+, 影劇館+) read as operators too, see pangu.js ADR 0013
    assert space_text("公視+上架了新片") == "公視 + 上架了新片"
    assert space_text("MOD影劇館+上架了新片") == "MOD 影劇館 + 上架了新片"

    # DO NOT change if already spacing
    assert space_text("前面 + 後面") == "前面 + 後面"
    assert space_text("Vinta + Mollie") == "Vinta + Mollie"
    assert space_text("Vinta + 陳上進") == "Vinta + 陳上進"
    assert space_text("陳上進 + Vinta") == "陳上進 + Vinta"
    assert space_text("得到一個 A + B 的結果") == "得到一個 A + B 的結果"


# A plus with half-width characters on both sides binds them into one token,
# spaced from CJK as a unit and never split
def test_handle_symbol_as_plus_token():
    assert space_text("Vinta+Mollie") == "Vinta+Mollie"  # If no CJK, DO NOT change
    assert space_text("得到一個A+B的結果") == "得到一個 A+B 的結果"
    assert space_text("答案是5+5的和") == "答案是 5+5 的和"


def test_handle_symbol_as_special_case():
    assert space_text("得到一個A+的結果") == "得到一個 A+ 的結果"
    assert space_text("得到一個 A+ 的結果") == "得到一個 A+ 的結果"
    assert space_text("得到一個C++的結果") == "得到一個 C++ 的結果"
    assert space_text("得到一個 C++的結果") == "得到一個 C++ 的結果"
    assert space_text("得到一個i++的結果") == "得到一個 i++ 的結果"
    assert space_text("成績是A+的等級") == "成績是 A+ 的等級"
    assert space_text("我會寫C++的程式") == "我會寫 C++ 的程式"

    assert space_text("打+886這個號碼") == "打 +886 這個號碼"
    assert space_text("氣溫是+5度左右") == "氣溫是 +5 度左右"

    assert space_text("Disney+上架了新片") == "Disney+ 上架了新片"
    assert space_text("Apple TV+上架了新片") == "Apple TV+ 上架了新片"
    assert space_text("有100+的選擇") == "有 100+ 的選擇"
    assert space_text("這裡有18+的內容") == "這裡有 18+ 的內容"


# FIXME
# def test_handle_symbol_in_real_world_bundle_plans():
#     assert space_text("【速在必行方案】HiNet光世代+Wi-Fi全屋通1台+MOD影劇館+(300M/300M)") == "【速在必行方案】HiNet 光世代 + Wi-Fi 全屋通 1 台 + MOD 影劇館+ (300M/300M)"
#
#     assert space_text("HiNet光世代+MOD+影劇館+/全選/自選20/特選餐/豪華餐(5選1)+Wi-Fi全屋通(1台)") == "HiNet 光世代 + MOD + 影劇館+/全選/自選 20/特選餐/豪華餐 (5 選 1) + Wi-Fi 全屋通 (1 台)"
