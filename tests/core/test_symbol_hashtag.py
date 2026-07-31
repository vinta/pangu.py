from pangu import spacing_text


# Symbol # only add space on the left
def test_handle_symbol_as_hashtag():
    assert spacing_text("前面#後面") == "前面 #後面"
    assert spacing_text("前面#H2G2後面") == "前面 #H2G2 後面"
    assert spacing_text("前面 #銀河便車指南 後面") == "前面 #銀河便車指南 後面"
    assert spacing_text("前面#銀河便車指南 後面") == "前面 #銀河便車指南 後面"
    assert spacing_text("前面#銀河公車指南 #銀河拖吊車指南 後面") == "前面 #銀河公車指南 #銀河拖吊車指南 後面"

    # Special cases
    assert spacing_text("前面C#後面") == "前面 C# 後面"
    assert spacing_text("前面F#後面") == "前面 F# 後面"


def test_handle_symbols_as_weibo_like_hashtags():
    # FIXME
    # assert spacing_text("前面#H2G2#後面") == "前面 #H2G2# 後面"
    # assert spacing_text("前面#銀河閃電霹靂車指南#後面") == "前面 #銀河閃電霹靂車指南# 後面"
    pass
