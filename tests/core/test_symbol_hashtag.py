from pangu import space_text


def test_handle_symbol_as_hashtag():
    assert space_text("前面#後面") == "前面 #後面"
    assert space_text("前面#H2G2後面") == "前面 #H2G2 後面"
    assert space_text("前面 #銀河便車指南 後面") == "前面 #銀河便車指南 後面"
    assert space_text("前面#銀河便車指南 後面") == "前面 #銀河便車指南 後面"
    assert space_text("前面#銀河公車指南 #銀河拖吊車指南 後面") == "前面 #銀河公車指南 #銀河拖吊車指南 後面"


def test_handle_symbol_as_preserved_pattern():
    assert space_text("前面C#後面") == "前面 C# 後面"
    assert space_text("前面F#後面") == "前面 F# 後面"
    assert space_text("前端/後端/資料庫：C#和Python") == "前端/後端/資料庫：C# 和 Python"


def test_handle_symbol_as_hashtag_in_a_slash_list():
    assert space_text("dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/") == "dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/"
