from pangu import spacing_text


def test_handle_symbols_as_quotes():
    assert spacing_text('前面"中文123漢字"後面') == '前面 "中文 123 漢字" 後面'
    assert spacing_text('前面"中文123"後面') == '前面 "中文 123" 後面'
    assert spacing_text('前面"中文abc"後面') == '前面 "中文 abc" 後面'
    assert spacing_text('前面"123漢字"後面') == '前面 "123 漢字" 後面'
    assert spacing_text('前面"中文123" tail') == '前面 "中文 123" tail'
    assert spacing_text('head "中文123漢字"後面') == 'head "中文 123 漢字" 後面'
    assert spacing_text('head "中文123漢字" tail') == 'head "中文 123 漢字" tail'


def test_handle_adjacent_to_cjk():
    assert spacing_text('我們也不可以說"We invited the reverend to dinner."') == '我們也不可以說 "We invited the reverend to dinner."'
    assert spacing_text('"We invited the Rev. Darling."我們也不可以說') == '"We invited the Rev. Darling." 我們也不可以說'
    assert spacing_text('它應該這樣使用："We invited"') == '它應該這樣使用："We invited"'

    # Full paragraph with multiple quoted segments and solitary &nbsp; (\u00a0)
    assert (
        spacing_text(
            'Rev. (Reverend；牧師的尊稱)這個縮寫嚴格來說並不是一項頭銜，而是形容詞。所以，它應該這樣使用："We invited the Rev. Alan Darling." 或\u00a0 "We\u00a0invited the Rev. Mr. Darling."，而非"We invited the Rev. Darling."我們也不可以說"We invited the reverend to dinner." -- Only a cad would invite the rev. (只有下流的人才會招致批評：句中的 rev. 是 review 的縮寫，算是雙關語)'
        )
        == 'Rev. (Reverend；牧師的尊稱) 這個縮寫嚴格來說並不是一項頭銜，而是形容詞。所以，它應該這樣使用："We invited the Rev. Alan Darling." 或\u00a0 "We\u00a0invited the Rev. Mr. Darling."，而非 "We invited the Rev. Darling." 我們也不可以說 "We invited the reverend to dinner." -- Only a cad would invite the rev. (只有下流的人才會招致批評：句中的 rev. 是 review 的縮寫，算是雙關語)'
    )


# The real paragraph from ananedu.com/yes928/writter/abbreviations.htm, whose text node keeps the line breaks of the wrapped HTML source. Its spacing is already correct, so it must come back untouched: the
# quoted segments span those newlines, and pairing them line by line would resync on the wrong quote and eat the spaces around 或 and ，而非
def test_handle_across_the_line_breaks_of_a_wrapped_html_source():
    assert spacing_text('使用："We\ninvited Darling." 或 "We invited."') == '使用："We\ninvited Darling." 或 "We invited."'

    text = 'Rev. (Reverend；牧師的尊稱) \n    這個縮寫嚴格來說並不是一項頭銜，而是形容詞。所以，它應該這樣使用："We \n    invited the Rev. Alan Darling." 或\u00a0 "We\u00a0 invited the Rev. Mr. \n    Darling." ，而非 "We invited the Rev. Darling." 我們也不可以說\u00a0 \n    "We invited the reverend to dinner." -- Only a cad would invite the rev. (只有下流的人才會招致批評：句中的 \n    rev. 是 review 的縮寫，算是雙關語) '
    assert spacing_text(text) == text


# Some input habits type both quotes of a pair as closing curly quotes,
# so a ”…” pair reads as opening/closing quotes when no unclosed “ precedes it
def test_handle_misused_quote_pairs():
    assert spacing_text("他说”你好”啊") == "他说 ”你好” 啊"

    assert (
        spacing_text("《战斧骨》里还有个镜头挺有意思，就是男主”见路不走”，不从峡谷入口走，而选择了从侧面翻越，还顺便借着口哨吸引出来一个食人族给杀了。")
        == "《战斧骨》里还有个镜头挺有意思，就是男主 ”见路不走”，不从峡谷入口走，而选择了从侧面翻越，还顺便借着口哨吸引出来一个食人族给杀了。"
    )


# FIXME
# Straight quotes cannot distinguish opening from closing, so quotes are paired left-to-right. Text whose first quote is already a closing quote shifts the pairing for everything after it, and the CJK prose
# between two quoted segments is then treated as quoted content whose edge spaces get stripped. See #287
def test_handle_mis_pairing_known_limitation():
    assert spacing_text('Darling." 或 "We') == 'Darling."或" We'
