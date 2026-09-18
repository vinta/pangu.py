import pytest

from pangu import space_text


def test_handle_symbol_as_operator():
    assert space_text("前面+後面") == "前面 + 後面"
    assert space_text("陳上進+Vinta") == "陳上進 + Vinta"
    assert space_text("Vinta+陳上進") == "Vinta + 陳上進"
    assert space_text("你+我=我們") == "你 + 我 = 我們"
    assert space_text("Switch+健身環套組") == "Switch + 健身環套組"
    assert space_text("MacBook Air M2+滑鼠組合") == "MacBook Air M2 + 滑鼠組合"

    # DO NOT change if already spacing
    assert space_text("前面 + 後面") == "前面 + 後面"
    assert space_text("Vinta + Abc123") == "Vinta + Abc123"
    assert space_text("Vinta + 陳上進") == "Vinta + 陳上進"
    assert space_text("陳上進 + Vinta") == "陳上進 + Vinta"
    assert space_text("得到一個 A + B 的結果") == "得到一個 A + B 的結果"


def test_handle_symbol_as_separator():
    # A plus after a word in CJK contact is undecided by any affix, so plus reading spaces it as a separator, in a bundle plan and on a brand line alike
    assert space_text("Switch OLED+健身環+保護貼") == "Switch OLED + 健身環 + 保護貼"

    # Plus reading runs before the operator rules, so a CJK+A contact flips the line's later joiners too; a line with no contact keeps them
    assert space_text("陳上進+Vinta+Abc123") == "陳上進 + Vinta + Abc123"
    assert space_text("HiNet光世代+MOD+Wi-Fi全屋通") == "HiNet 光世代 + MOD + Wi-Fi 全屋通"
    assert space_text("套餐含MOD+Netflix+Disney") == "套餐含 MOD+Netflix+Disney"

    assert space_text("HiNet光世代+MOD+影劇館+/全選/自選20/特選餐/豪華餐(5選1)+Wi-Fi全屋通(1台)") == "HiNet 光世代 + MOD + 影劇館+/全選/自選 20/特選餐/豪華餐 (5 選 1) + Wi-Fi 全屋通 (1 台)"

    assert space_text("【速在必行方案】HiNet光世代+Wi-Fi全屋通1台+MOD影劇館+(300M/300M)") == "【速在必行方案】HiNet 光世代 + Wi-Fi 全屋通 1 台 + MOD 影劇館+ (300M/300M)"

    assert space_text("HiNet光世代+MOD+自選餐(全選)+「影劇館+」") == "HiNet 光世代 + MOD + 自選餐 (全選) +「影劇館+」"

    assert space_text("自選餐(全選)+「影劇館」") == "自選餐 (全選) +「影劇館」"


# FIXME
@pytest.mark.xfail(strict=True, reason="FIXME: it.todo upstream")
def test_handle_symbol_as_separator_after_a_product_name_ending_in_a_digit():
    assert space_text("Switch 2+瑪利歐賽車世界同捆組") == "Switch 2 + 瑪利歐賽車世界同捆組"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta+Abc123") == "Vinta+Abc123"  # If no CJK, DO NOT change
    assert space_text("前面A+B後面") == "前面 A+B 後面"
    assert space_text("得到一個A+B的結果") == "得到一個 A+B 的結果"
    assert space_text("答案是5+5的和") == "答案是 5+5 的和"


def test_handle_symbol_as_preserved_pattern():
    assert space_text("得到一個C++的結果") == "得到一個 C++ 的結果"
    assert space_text("得到一個 C++的結果") == "得到一個 C++ 的結果"
    assert space_text("得到一個i++的結果") == "得到一個 i++ 的結果"
    assert space_text("我會寫C++的程式") == "我會寫 C++ 的程式"


def test_handle_symbol_as_affix():
    # Grades
    assert space_text("得到一個A+的結果") == "得到一個 A+ 的結果"
    assert space_text("得到一個 A+ 的結果") == "得到一個 A+ 的結果"
    assert space_text("成績是A+的等級") == "成績是 A+ 的等級"

    # Sign before digits
    assert space_text("打+886這個號碼") == "打 +886 這個號碼"
    assert space_text("氣溫是+5度左右") == "氣溫是 +5 度左右"

    # Suffix after digits
    assert space_text("有100+的選擇") == "有 100+ 的選擇"
    assert space_text("這裡有18+的內容") == "這裡有 18+ 的內容"
    assert space_text("評分3.5+的餐廳") == "評分 3.5+ 的餐廳"
    assert space_text("Python 3+的版本") == "Python 3+ 的版本"
