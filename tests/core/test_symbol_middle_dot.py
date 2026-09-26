from pangu import space_text


# \u00b7
def test_handle_symbol():
    assert space_text("前面·後面") == "前面・後面"
    assert space_text("喬治·R·R·馬丁") == "喬治・R・R・馬丁"
    assert space_text("M·奈特·沙马兰") == "M・奈特・沙马兰"


def test_should_not_convert_if_already_spaced():
    assert space_text("哥爾 · D · 羅傑") == "哥爾 · D · 羅傑"
    assert space_text("看过 · · ·") == "看过 · · ·"
    assert space_text("看过 · · · (2026部)") == "看过 · · · (2026 部)"


# \u2022
def test_handle_symbol_2():
    assert space_text("前面•後面") == "前面・後面"
    assert space_text("喬治•R•R•馬丁") == "喬治・R・R・馬丁"
    assert space_text("M•奈特•沙马兰") == "M・奈特・沙马兰"


def test_should_not_convert_if_already_spaced_2():
    assert space_text("前面 • 後面") == "前面 • 後面"
    assert space_text("喬治 • R • R • 馬丁") == "喬治 • R • R • 馬丁"
    assert space_text("M • 奈特 • 沙马兰") == "M • 奈特 • 沙马兰"


def test_should_not_convert_consecutive_symbols():
    assert space_text("國泰CUBE卡 •••• 1234") == "國泰 CUBE 卡 •••• 1234"
    assert space_text("ether.fi Cash Card •••• 5678") == "ether.fi Cash Card •••• 5678"


# \u2027
def test_handle_symbol_3():
    assert space_text("前面‧後面") == "前面・後面"
    assert space_text("喬治‧R‧R‧馬丁") == "喬治・R・R・馬丁"
    assert space_text("M‧奈特‧沙马兰") == "M・奈特・沙马兰"


def test_should_not_convert_if_already_spaced_3():
    assert space_text("前面 ‧ 後面") == "前面 ‧ 後面"
    assert space_text("喬治 ‧ R ‧ R ‧ 馬丁") == "喬治 ‧ R ‧ R ‧ 馬丁"
    assert space_text("M ‧ 奈特 ‧ 沙马兰") == "M ‧ 奈特 ‧ 沙马兰"
