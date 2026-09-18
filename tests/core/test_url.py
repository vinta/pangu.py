import pytest

from pangu import space_text


def test_leave_the_inside_of_a_url_untouched():
    # Issue https://github.com/vinta/pangu.js/issues/147
    assert space_text("第三條的內容為http://se.360.cn/") == "第三條的內容為 http://se.360.cn/"

    # Issue https://github.com/vinta/pangu.js/issues/149
    assert space_text("你https://%E5%A6%82") == "你 https://%E5%A6%82"

    # Issue https://github.com/vinta/pangu.js/issues/155
    assert space_text("https://xxxxx/自动加空格.html") == "https://xxxxx/自动加空格.html"

    assert (
        space_text("打開此連結，https://www.google.com/search?q=%E5%9B%BD%E5%AF%86SM2%2F3%2F4%E7%AE%97%E6%B3%95+360")
        == "打開此連結，https://www.google.com/search?q=%E5%9B%BD%E5%AF%86SM2%2F3%2F4%E7%AE%97%E6%B3%95+360"
    )

    assert space_text("https://www.google.com/search?q=中文&hl=zh-TW") == "https://www.google.com/search?q=中文&hl=zh-TW"

    assert space_text("https://zh.wikipedia.org/w/index.php?title=中文&action=history") == "https://zh.wikipedia.org/w/index.php?title=中文&action=history"

    assert space_text("網址是https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%96%87") == "網址是 https://zh.wikipedia.org/wiki/%E4%B8%AD%E6%96%87"

    assert space_text("https://zh.wikipedia.org/wiki/中文#歷史") == "https://zh.wikipedia.org/wiki/中文#歷史"

    assert space_text("參考https://zh.wikipedia.org/wiki/中文#歷史的說明") == "參考 https://zh.wikipedia.org/wiki/中文#歷史的說明"

    assert space_text("https://zh.wikipedia.org/wiki/盤古") == "https://zh.wikipedia.org/wiki/盤古"


# FIXME: CJK characters continue the URL, and no rule tells URL-internal CJK from prose written tight after the URL. See pangu.js ADR 0026
@pytest.mark.xfail(strict=True, reason="FIXME: it.todo upstream")
def test_space_a_url_from_cjk_on_both_sides():
    assert space_text("搜尋https://www.google.com/search?q=pangu.js&hl=zh-TW看看") == "搜尋 https://www.google.com/search?q=pangu.js&hl=zh-TW 看看"

    assert space_text("看https://github.com/vinta/pangu.js/issues/155這個issue") == "看 https://github.com/vinta/pangu.js/issues/155 這個 issue"

    assert space_text("文件在https://developer.mozilla.org/zh-TW/docs/Web/API/URL/canParse_static這裡") == "文件在 https://developer.mozilla.org/zh-TW/docs/Web/API/URL/canParse_static 這裡"


def test_stop_a_url_at_cjk_punctuation_quotes_and_brackets():
    assert space_text("請看https://vinta.ws/code/。") == "請看 https://vinta.ws/code/。"

    assert space_text("請看https://vinta.ws/code/，謝謝") == "請看 https://vinta.ws/code/，謝謝"

    assert space_text("（https://vinta.ws/code/）") == "（https://vinta.ws/code/）"

    assert space_text("(https://vinta.ws/code/)") == "(https://vinta.ws/code/)"

    assert space_text("「https://vinta.ws/code/」") == "「https://vinta.ws/code/」"


def test_leave_trailing_half_width_punctuation_outside_the_url():
    assert space_text("詳見https://vinta.ws/code/.") == "詳見 https://vinta.ws/code/."


def test_leave_a_url_inside_an_attribute_value_untouched():
    assert space_text('<a href="https://zh.wikipedia.org/wiki/中文#歷史">中文</a>') == '<a href="https://zh.wikipedia.org/wiki/中文#歷史">中文</a>'

    assert (
        space_text('<a href="http://vinta.ws/中文網址with英文.html">oh一個超連結with英文，網址包含中文</a>')
        == '<a href="http://vinta.ws/中文網址with英文.html">oh 一個超連結 with 英文，網址包含中文</a>'
    )


def test_space_a_hashtag_on_a_line_that_also_holds_a_url():
    assert space_text("看完這篇#pangu 的介紹 https://vinta.ws/code/") == "看完這篇 #pangu 的介紹 https://vinta.ws/code/"


def test_leave_a_url_with_no_cjk_contact_untouched():
    assert space_text("see https://vinta.ws/code/ and 中文") == "see https://vinta.ws/code/ and 中文"
