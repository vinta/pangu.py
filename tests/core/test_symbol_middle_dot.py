from pangu import space_text


# \u00b7
def test_handle_symbol():
    assert space_text("前面·後面") == "前面・後面"
    assert space_text("喬治·R·R·馬丁") == "喬治・R・R・馬丁"
    assert space_text("M·奈特·沙马兰") == "M・奈特・沙马兰"


# \u2022
def test_handle_symbol_2():
    assert space_text("前面•後面") == "前面・後面"
    assert space_text("喬治•R•R•馬丁") == "喬治・R・R・馬丁"
    assert space_text("M•奈特•沙马兰") == "M・奈特・沙马兰"


# \u2027
def test_handle_symbol_3():
    assert space_text("前面‧後面") == "前面・後面"
    assert space_text("喬治‧R‧R‧馬丁") == "喬治・R・R・馬丁"
    assert space_text("M‧奈特‧沙马兰") == "M・奈特・沙马兰"
