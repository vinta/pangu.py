from pangu import spacing_text


def test_handle_short_text():
    assert spacing_text("中a") == "中 a"
    assert spacing_text("a中") == "a 中"
    assert spacing_text("1中") == "1 中"
    assert spacing_text("中1") == "中 1"
    assert spacing_text("中a1") == "中 a1"
    assert spacing_text("a1中") == "a1 中"
    assert spacing_text("a中1") == "a 中 1"
    assert spacing_text("1中a") == "1 中 a"


def test_handle_alphabets():
    assert spacing_text("中文abc") == "中文 abc"
    assert spacing_text("abc中文") == "abc 中文"


def test_handle_numbers():
    assert spacing_text("中文123") == "中文 123"
    assert spacing_text("123中文") == "123 中文"


# https://symbl.cc/en/unicode-table/#latin-1-supplement
def test_handle_latin_1_supplement():
    assert spacing_text("中文Ø漢字") == "中文 Ø 漢字"
    assert spacing_text("中文 Ø 漢字") == "中文 Ø 漢字"


# https://symbl.cc/en/unicode-table/#greek-coptic
def test_handle_greek_and_coptic():
    assert spacing_text("中文β漢字") == "中文 β 漢字"
    assert spacing_text("中文 β 漢字") == "中文 β 漢字"
    assert spacing_text("我是α，我是Ω") == "我是 α，我是 Ω"


# https://symbl.cc/en/unicode-table/#number-forms
def test_handle_number_forms():
    assert spacing_text("中文Ⅶ漢字") == "中文 Ⅶ 漢字"
    assert spacing_text("中文 Ⅶ 漢字") == "中文 Ⅶ 漢字"


# https://symbl.cc/en/unicode-table/#cjk-radicals-supplement
def test_handle_cjk_radicals_supplement():
    assert spacing_text("abc⻤123") == "abc ⻤ 123"
    assert spacing_text("abc ⻤ 123") == "abc ⻤ 123"


# https://symbl.cc/en/unicode-table/#kangxi-radicals
def test_handle_kangxi_radicals():
    assert spacing_text("abc⾗123") == "abc ⾗ 123"
    assert spacing_text("abc ⾗ 123") == "abc ⾗ 123"


# https://symbl.cc/en/unicode-table/#hiragana
def test_handle_hiragana():
    assert spacing_text("abcあ123") == "abc あ 123"
    assert spacing_text("abc あ 123") == "abc あ 123"


# https://symbl.cc/en/unicode-table/#katakana
def test_handle_katakana():
    assert spacing_text("abcア123") == "abc ア 123"
    assert spacing_text("abc ア 123") == "abc ア 123"


# https://symbl.cc/en/unicode-table/#bopomofo
def test_handle_bopomofo():
    assert spacing_text("abcㄅ123") == "abc ㄅ 123"
    assert spacing_text("abc ㄅ 123") == "abc ㄅ 123"


# https://symbl.cc/en/unicode-table/#enclosed-cjk-letters-and-months
def test_handle_enclosed_cjk_letters_and_months():
    assert spacing_text("abc㈱123") == "abc ㈱ 123"
    assert spacing_text("abc ㈱ 123") == "abc ㈱ 123"


# https://symbl.cc/en/unicode-table/#cjk-unified-ideographs-extension-a
def test_handle_cjk_unified_ideographs_extension_a():
    assert spacing_text("abc㐂123") == "abc 㐂 123"
    assert spacing_text("abc 㐂 123") == "abc 㐂 123"


# https://symbl.cc/en/unicode-table/#cjk-unified-ideographs
def test_handle_cjk_unified_ideographs():
    assert spacing_text("abc丁123") == "abc 丁 123"
    assert spacing_text("abc 丁 123") == "abc 丁 123"


# https://symbl.cc/en/unicode-table/#cjk-compatibility-ideographs
def test_handle_cjk_compatibility_ideographs():
    assert spacing_text("abc車123") == "abc 車 123"
    assert spacing_text("abc 車 123") == "abc 車 123"
