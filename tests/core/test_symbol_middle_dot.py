from pangu import spacing_text


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
