from pangu import space_text


def test_handle_solitary_nbsp():
    # The &nbsp; already separates the runs it sits between, so only the genuinely missing 說|We junction gets a space
    assert space_text("我們說We\u00a0invited") == "我們說 We\u00a0invited"
    assert space_text("第\u00a05\u00a0章") == "第\u00a05\u00a0章"


def test_handle_solitary_nbsp_adjacent_to_a_half_width_space():
    # A doubled gap the author wrote. CSS collapses two half-width spaces but never collapses &nbsp; + space, so this paints wider than one space.
    # Dropping either character would be a rewrite, so both stay
    assert space_text('或\u00a0 "We invited"') == '或\u00a0 "We invited"'


def test_handle_consecutive_nbsp():
    # Runs of 2+ &nbsp;s are deliberate formatting (e.g. paragraph indentation)
    assert space_text("中文\u00a0\u00a0\u00a0\u00a0中文") == "中文\u00a0\u00a0\u00a0\u00a0中文"


def test_handle_nbsp_adjacent_to_other_whitespace():
    assert space_text("中文\u00a0\n中文") == "中文\u00a0\n中文"


def test_handle_nbsp_at_string_boundaries():
    assert space_text("\u00a0中文abc") == "\u00a0中文 abc"
    assert space_text("中文abc\u00a0") == "中文 abc\u00a0"


def test_handle_nbsp_separating_a_hashtag_from_cjk():
    # The hashtag guard has to read an &nbsp; as the gap it is, otherwise the # reads as glued to 台北 and gets split off
    assert space_text("台北\u00a0#中文") == "台北\u00a0#中文"
    assert space_text("中文#\u00a0abc") == "中文#\u00a0abc"
