from pangu import space_text


def test_handle_product_names_with_suffixes():
    assert space_text("Apple Fitness+推出新課程") == "Apple Fitness+ 推出新課程"
    assert space_text("Apple TV+上架了新片") == "Apple TV+ 上架了新片"
    assert space_text("Discovery+和discovery+都上架了") == "Discovery+ 和 discovery+ 都上架了"
    assert space_text("Disney+上架了新片") == "Disney+ 上架了新片"
    assert space_text("Disney+上架了C++課程") == "Disney+ 上架了 C++ 課程"
    assert space_text("PS+會員") == "PS+ 會員"
    assert space_text("公視+上架了新片") == "公視+ 上架了新片"
    assert space_text("如何使用PTS+（公視+）註冊與觀看？") == "如何使用 PTS+（公視+）註冊與觀看？"
    assert space_text("公視+(免費平台)") == "公視+ (免費平台)"
    assert space_text("今天來看公視+") == "今天來看公視+"
    assert space_text("MOD影劇館+上架了新片") == "MOD 影劇館+ 上架了新片"
    assert space_text("Netflix、Disney+、Apple TV+、MOD影劇館+、公視+等串流平台") == "Netflix、Disney+、Apple TV+、MOD 影劇館+、公視+ 等串流平台"


def test_handle_product_tiers_with_suffixes():
    assert space_text("vivo X70 Pro+開賣") == "vivo X70 Pro+ 開賣"


def test_handle_credit_ratings_with_suffixes():
    assert space_text("評等介於AA-和AA+之間") == "評等介於 AA- 和 AA+ 之間"
    assert space_text("惠譽給予BBB+評等") == "惠譽給予 BBB+ 評等"
    assert space_text("惠譽給予BBB-評等") == "惠譽給予 BBB- 評等"
    assert space_text("中華信評給予twAA+評等") == "中華信評給予 twAA+ 評等"


def test_handle_blood_types_with_suffixes():
    assert space_text("血型是AB+的人") == "血型是 AB+ 的人"
    assert space_text("血型是AB-的人") == "血型是 AB- 的人"
    assert space_text("血型是Rh+的人") == "血型是 Rh+ 的人"
    assert space_text("血型是Rh-的人") == "血型是 Rh- 的人"
    assert space_text("型號AB-123的零件，血型是AB-的人") == "型號 AB-123 的零件，血型是 AB- 的人"


def test_handle_closing_punctuation_tight_after_a_suffixes():
    assert space_text("公視+，今天有新片") == "公視+，今天有新片"
    assert space_text("公視+。") == "公視+。"
    assert space_text("(公視+）") == "(公視+）"
    assert space_text("[公視+]") == "[公視+]"
    assert space_text("「公視+」") == "「公視+」"


def test_handle_non_preserved_names():
    assert space_text("私視+上線") == "私視 + 上線"
    assert space_text("Disney-上架了新片") == "Disney - 上架了新片"
