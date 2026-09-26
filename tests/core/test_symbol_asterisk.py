from pangu import space_text


def test_handle_symbol_as_operator():
    assert space_text("前面*後面") == "前面 * 後面"
    assert space_text("Vinta*陳上進") == "Vinta * 陳上進"
    assert space_text("陳上進*Vinta") == "陳上進 * Vinta"
    assert space_text("標示*的欄位代表必填") == "標示 * 的欄位代表必填"
    assert space_text("時薪*(平日時數+假日時數)") == "時薪 * (平日時數 + 假日時數)"

    # Rare cases, ignore
    # assert space_text("時薪*[平日時數+假日時數]") == "時薪 * [平日時數 + 假日時數]"
    # assert space_text("係數*[2+3]") == "係數 * [2+3]"
    # assert space_text("係數*[abc]") == "係數 * [abc]"
    # assert space_text("係數*[[0-9].log]") == "係數 * [[0-9].log]"

    # DO NOT change if already spacing
    assert space_text("前面 * 後面") == "前面 * 後面"
    assert space_text("Vinta * Abc123") == "Vinta * Abc123"
    assert space_text("Vinta * 陳上進") == "Vinta * 陳上進"
    assert space_text("陳上進 * Vinta") == "陳上進 * Vinta"
    assert space_text("得到一個 A * B 的結果") == "得到一個 A * B 的結果"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta*Abc123") == "Vinta*Abc123"  # If no CJK, DO NOT change
    assert space_text("得到一個A*B的結果") == "得到一個 A*B 的結果"
    assert space_text("算式是2*3的積") == "算式是 2*3 的積"


def test_handle_symbol_as_preserved_pattern():
    assert space_text("刪掉*.log的檔案") == "刪掉 *.log 的檔案"


def test_preserve_bracket_globs():
    assert space_text("刪掉*[0-9].log的檔案") == "刪掉 *[0-9].log 的檔案"
    assert space_text("刪掉*[a-z].log的檔案") == "刪掉 *[a-z].log 的檔案"
    assert space_text("刪掉*[!0-9].log的檔案") == "刪掉 *[!0-9].log 的檔案"
    assert space_text("刪掉*[0-9].tar.gz的檔案") == "刪掉 *[0-9].tar.gz 的檔案"
    assert space_text("刪掉*[0-9][0-9].log的檔案") == "刪掉 *[0-9][0-9].log 的檔案"
    assert space_text("刪掉*[0-9]*.log的檔案") == "刪掉 *[0-9]*.log 的檔案"

    # DO NOT change if already spacing
    assert space_text("刪掉 *[0-9].log 的檔案") == "刪掉 *[0-9].log 的檔案"
    assert space_text("刪掉 *[a-z].log 的檔案") == "刪掉 *[a-z].log 的檔案"
    assert space_text("刪掉 *[!0-9].log 的檔案") == "刪掉 *[!0-9].log 的檔案"
    assert space_text("刪掉 *[0-9].tar.gz 的檔案") == "刪掉 *[0-9].tar.gz 的檔案"
    assert space_text("刪掉 *[0-9][0-9].log 的檔案") == "刪掉 *[0-9][0-9].log 的檔案"
    assert space_text("刪掉 *[0-9]*.log 的檔案") == "刪掉 *[0-9]*.log 的檔案"
