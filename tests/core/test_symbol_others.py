from pangu import spacing_text


# \u2026
def test_handle_symbol_only_add_space_on_the_right():
    assert spacing_text("前面…後面") == "前面… 後面"
    assert spacing_text("前面……後面") == "前面…… 後面"


# \u00b7
def test_handle_symbol_replace_with():
    assert spacing_text("前面·後面") == "前面・後面"
    assert spacing_text("喬治·R·R·馬丁") == "喬治・R・R・馬丁"
    assert spacing_text("M·奈特·沙马兰") == "M・奈特・沙马兰"


# \u2022
def test_handle_symbol_replace_with_2():
    assert spacing_text("前面•後面") == "前面・後面"
    assert spacing_text("喬治•R•R•馬丁") == "喬治・R・R・馬丁"
    assert spacing_text("M•奈特•沙马兰") == "M・奈特・沙马兰"


# \u2027
def test_handle_symbol_replace_with_3():
    assert spacing_text("前面‧後面") == "前面・後面"
    assert spacing_text("喬治‧R‧R‧馬丁") == "喬治・R・R・馬丁"
    assert spacing_text("M‧奈特‧沙马兰") == "M・奈特・沙马兰"


# \u201c
# \u201d
def test_handle_english_with_symbols():
    assert spacing_text("阿里云开源“计算王牌”Blink，实时计算时代已来") == "阿里云开源 “计算王牌” Blink，实时计算时代已来"

    assert spacing_text("苹果撤销Facebook“企业证书”后者股价一度短线走低") == "苹果撤销 Facebook “企业证书” 后者股价一度短线走低"

    assert spacing_text("【UCG中字】“數毛社”DF的《戰神4》全新演示解析") == "【UCG 中字】“數毛社” DF 的《戰神 4》全新演示解析"


# ✀-➿
def test_handle_dingbats_symbols_add_space_between_them_and_cjk():
    assert spacing_text("剪刀✂符號") == "剪刀 ✂ 符號"
    assert spacing_text("完成✅了") == "完成 ✅ 了"
    assert spacing_text("愛心❤符號") == "愛心 ❤ 符號"


# — An em-dash is not a spaced half-width symbol, so it stays flush against CJK
def test_handle_em_dash_does_not_add_space_with_cjk():
    assert spacing_text("前面—後面") == "前面—後面"
    assert spacing_text("他說——不對") == "他說——不對"
