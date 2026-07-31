from pangu import spacing_text


#
# Symbol &nbsp; suppresses spacing, always preserve
def test_handle_solitary_nbsp_preserve():
    # The &nbsp; already separates the runs it sits between, so only the genuinely missing 說|We junction gets a space
    assert spacing_text("我們說We\u00a0invited") == "我們說 We\u00a0invited"
    assert spacing_text("第\u00a05\u00a0章") == "第\u00a05\u00a0章"


def test_handle_solitary_nbsp_adjacent_to_a_half_width_space_preserve():
    # A doubled gap the author wrote. CSS collapses two half-width spaces but never collapses &nbsp; + space, so this paints wider than one space.
    # Dropping either character would be a rewrite, so both stay
    assert spacing_text('或\u00a0 "We invited"') == '或\u00a0 "We invited"'


def test_handle_consecutive_nbsp_preserve():
    # Runs of 2+ &nbsp;s are deliberate formatting (e.g. paragraph indentation)
    assert spacing_text("中文\u00a0\u00a0\u00a0\u00a0中文") == "中文\u00a0\u00a0\u00a0\u00a0中文"


def test_handle_nbsp_adjacent_to_other_whitespace_preserve():
    assert spacing_text("中文\u00a0\n中文") == "中文\u00a0\n中文"


def test_handle_nbsp_at_string_boundaries_preserve():
    assert spacing_text("\u00a0中文abc") == "\u00a0中文 abc"
    assert spacing_text("中文abc\u00a0") == "中文 abc\u00a0"


def test_handle_nbsp_separating_a_hashtag_from_cjk_preserve():
    # The hashtag guard has to read an &nbsp; as the gap it is, otherwise the # reads as glued to 台北 and gets split off
    assert spacing_text("台北\u00a0#中文") == "台北\u00a0#中文"
    assert spacing_text("中文#\u00a0abc") == "中文#\u00a0abc"
