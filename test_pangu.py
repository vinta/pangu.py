# coding: utf-8

import unittest

import pangu


class PanguTestCase(unittest.TestCase):
    def test_spacing(self):
        self.assertEqual(pangu.spacing('新八的構造成分有95%是眼鏡、3%是水、2%是垃圾'), u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾')
        self.assertEqual(pangu.spacing(u'新八的構造成分有95%是眼鏡、3%是水、2%是垃圾'), u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾')

        self.assertEqual(pangu.spacing('所以,請問Jackey的鼻子有幾個?3.14個!'), u'所以, 請問 Jackey 的鼻子有幾個? 3.14 個!')
        self.assertEqual(pangu.spacing(u'所以,請問Jackey的鼻子有幾個?3.14個!'), u'所以, 請問 Jackey 的鼻子有幾個? 3.14 個!')

        self.assertEqual(pangu.spacing('JUST WE就是JUST WE，既不偉大也不卑微！'), u'JUST WE 就是 JUST WE，既不偉大也不卑微！')
        self.assertEqual(pangu.spacing(u'JUST WE就是JUST WE，既不偉大也不卑微！'), u'JUST WE 就是 JUST WE，既不偉大也不卑微！')

        self.assertEqual(pangu.spacing('搭載MP3播放器，連續播放時數最長達到124小時的超強利刃……菊一文字RX-7!'), u'搭載 MP3 播放器，連續播放時數最長達到 124 小時的超強利刃…… 菊一文字 RX-7!')
        self.assertEqual(pangu.spacing(u'搭載MP3播放器，連續播放時數最長達到124小時的超強利刃……菊一文字RX-7!'), u'搭載 MP3 播放器，連續播放時數最長達到 124 小時的超強利刃…… 菊一文字 RX-7!')

        self.assertEqual(pangu.spacing('V'), u'V')

    def test_spacing_text(self):
        self.assertEqual(pangu.spacing("Mr.龍島主道：「Let's Party!各位高明博雅君子！」"), u"Mr. 龍島主道：「Let's Party! 各位高明博雅君子！」")

    def test_latin1_supplement(self):
        self.assertEqual(pangu.spacing('中文Ø漢字'), u'中文 Ø 漢字')
        self.assertEqual(pangu.spacing('中文 Ø 漢字'), u'中文 Ø 漢字')

    def test_general_punctuation(self):
        self.assertEqual(pangu.spacing('中文•漢字'), u'中文 • 漢字')
        self.assertEqual(pangu.spacing('中文 • 漢字'), u'中文 • 漢字')

    def test_number_forms(self):
        self.assertEqual(pangu.spacing('中文Ⅶ漢字'), u'中文 Ⅶ 漢字')
        self.assertEqual(pangu.spacing('中文 Ⅶ 漢字'), u'中文 Ⅶ 漢字')

    def test_cjk_radicals_supplement(self):
        self.assertEqual(pangu.spacing('abc⻤123'), u'abc ⻤ 123')
        self.assertEqual(pangu.spacing('abc ⻤ 123'), u'abc ⻤ 123')

    def test_kangxi_radicals(self):
        self.assertEqual(pangu.spacing('abc⾗123'), u'abc ⾗ 123')
        self.assertEqual(pangu.spacing('abc ⾗ 123'), u'abc ⾗ 123')

    def test_hiragana(self):
        self.assertEqual(pangu.spacing('abcあ123'), u'abc あ 123')
        self.assertEqual(pangu.spacing('abc あ 123'), u'abc あ 123')

    def test_katakana(self):
        self.assertEqual(pangu.spacing('abcア123'), u'abc ア 123')
        self.assertEqual(pangu.spacing('abc ア 123'), u'abc ア 123')

    def test_bopomofo(self):
        self.assertEqual(pangu.spacing('abcㄅ123'), u'abc ㄅ 123')
        self.assertEqual(pangu.spacing('abc ㄅ 123'), u'abc ㄅ 123')

    def test_enclosed_cjk_letters_and_months(self):
        self.assertEqual(pangu.spacing('abc㈱123'), u'abc ㈱ 123')
        self.assertEqual(pangu.spacing('abc ㈱ 123'), u'abc ㈱ 123')

    def test_cjk_unified_ideographs_extension_a(self):
        self.assertEqual(pangu.spacing('abc㐂123'), u'abc 㐂 123')
        self.assertEqual(pangu.spacing('abc 㐂 123'), u'abc 㐂 123')

    def test_cjk_unified_ideographs(self):
        self.assertEqual(pangu.spacing('abc丁123'), u'abc 丁 123')
        self.assertEqual(pangu.spacing('abc 丁 123'), u'abc 丁 123')

    def test_cjk_compatibility_ideographs(self):
        self.assertEqual(pangu.spacing('abc車123'), u'abc 車 123')
        self.assertEqual(pangu.spacing('abc 車 123'), u'abc 車 123')

    def test_tilde(self):
        self.assertEqual(pangu.spacing('前面~後面'), u'前面~ 後面')
        self.assertEqual(pangu.spacing('前面 ~ 後面'), u'前面 ~ 後面')
        self.assertEqual(pangu.spacing('前面~ 後面'), u'前面~ 後面')

    def test_back_quote(self):
        self.assertEqual(pangu.spacing('前面`後面'), u'前面 ` 後面')
        self.assertEqual(pangu.spacing('前面 ` 後面'), u'前面 ` 後面')
        self.assertEqual(pangu.spacing('前面` 後面'), u'前面 ` 後面')

    def test_exclamation_mark(self):
        self.assertEqual(pangu.spacing('前面!後面'), u'前面! 後面')
        self.assertEqual(pangu.spacing('前面 ! 後面'), u'前面 ! 後面')
        self.assertEqual(pangu.spacing('前面! 後面'), u'前面! 後面')

    def test_at(self):
        # https://twitter.com/vinta
        self.assertEqual(pangu.spacing('前面@vinta後面'), u'前面 @vinta 後面')
        self.assertEqual(pangu.spacing('前面 @vinta 後面'), u'前面 @vinta 後面')

        # http://weibo.com/vintalines
        self.assertEqual(pangu.spacing('前面@陳上進 後面'), u'前面 @陳上進 後面')
        self.assertEqual(pangu.spacing('前面 @陳上進 後面'), u'前面 @陳上進 後面')
        self.assertEqual(pangu.spacing('前面 @陳上進tail'), u'前面 @陳上進 tail')

    def test_hash(self):
        self.assertEqual(pangu.spacing('前面#H2G2後面'), u'前面 #H2G2 後面')
        self.assertEqual(pangu.spacing('前面#銀河便車指南 後面'), u'前面 #銀河便車指南 後面')
        self.assertEqual(pangu.spacing('前面#銀河便車指南tail'), u'前面 #銀河便車指南 tail')
        self.assertEqual(pangu.spacing('前面#銀河公車指南 #銀河拖吊車指南 後面'), u'前面 #銀河公車指南 #銀河拖吊車指南 後面')
        self.assertEqual(pangu.spacing('前面#H2G2#後面'), u'前面 #H2G2# 後面')
        self.assertEqual(pangu.spacing('前面#銀河閃電霹靂車指南#後面'), u'前面 #銀河閃電霹靂車指南# 後面')

    def test_dollar(self):
        self.assertEqual(pangu.spacing('前面$後面'), u'前面 $ 後面')
        self.assertEqual(pangu.spacing('前面 $ 後面'), u'前面 $ 後面')
        self.assertEqual(pangu.spacing('前面$100後面'), u'前面 $100 後面')

    def test_percent(self):
        self.assertEqual(pangu.spacing('前面%後面'), u'前面 % 後面')
        self.assertEqual(pangu.spacing('前面 % 後面'), u'前面 % 後面')
        self.assertEqual(pangu.spacing('前面100%後面'), u'前面 100% 後面')

    def test_caret(self):
        self.assertEqual(pangu.spacing('前面^後面'), u'前面 ^ 後面')
        self.assertEqual(pangu.spacing('前面 ^ 後面'), u'前面 ^ 後面')

    def test_ampersand(self):
        self.assertEqual(pangu.spacing('前面&後面'), u'前面 & 後面')
        self.assertEqual(pangu.spacing('前面 & 後面'), u'前面 & 後面')
        self.assertEqual(pangu.spacing('Vinta&Mollie'), u'Vinta&Mollie')
        self.assertEqual(pangu.spacing('Vinta&陳上進'), u'Vinta & 陳上進')
        self.assertEqual(pangu.spacing('陳上進&Vinta'), u'陳上進 & Vinta')
        self.assertEqual(pangu.spacing('得到一個A&B的結果'), u'得到一個 A&B 的結果')

    def test_asterisk(self):
        self.assertEqual(pangu.spacing('前面*後面'), u'前面 * 後面')
        self.assertEqual(pangu.spacing('前面 * 後面'), u'前面 * 後面')
        self.assertEqual(pangu.spacing('Vinta*Mollie'), u'Vinta*Mollie')
        self.assertEqual(pangu.spacing('Vinta*陳上進'), u'Vinta * 陳上進')
        self.assertEqual(pangu.spacing('陳上進*Vinta'), u'陳上進 * Vinta')
        self.assertEqual(pangu.spacing('得到一個A*B的結果'), u'得到一個 A*B 的結果')

    def test_parentheses(self):
        self.assertEqual(pangu.spacing('前面(中文123漢字)後面'), u'前面 (中文 123 漢字) 後面')
        self.assertEqual(pangu.spacing('前面(中文123)後面'), u'前面 (中文 123) 後面')
        self.assertEqual(pangu.spacing('前面(123漢字)後面'), u'前面 (123 漢字) 後面')
        self.assertEqual(pangu.spacing('前面(中文123漢字) tail'), u'前面 (中文 123 漢字) tail')
        self.assertEqual(pangu.spacing('head (中文123漢字)後面'), u'head (中文 123 漢字) 後面')
        self.assertEqual(pangu.spacing('head (中文123漢字) tail'), u'head (中文 123 漢字) tail')

    def test_minus(self):
        self.assertEqual(pangu.spacing('前面-後面'), u'前面 - 後面')
        self.assertEqual(pangu.spacing('前面 - 後面'), u'前面 - 後面')
        self.assertEqual(pangu.spacing('Vinta-Mollie'), u'Vinta-Mollie')
        self.assertEqual(pangu.spacing('Vinta-陳上進'), u'Vinta - 陳上進')
        self.assertEqual(pangu.spacing('陳上進-Vinta'), u'陳上進 - Vinta')
        self.assertEqual(pangu.spacing('得到一個A-B的結果'), u'得到一個 A-B 的結果')

    def test_underscore(self):
        self.assertEqual(pangu.spacing('前面_後面'), u'前面_後面')
        self.assertEqual(pangu.spacing('前面 _ 後面'), u'前面 _ 後面')

    def test_plus(self):
        self.assertEqual(pangu.spacing('前面+後面'), u'前面 + 後面')
        self.assertEqual(pangu.spacing('前面 + 後面'), u'前面 + 後面')
        self.assertEqual(pangu.spacing('Vinta+Mollie'), u'Vinta+Mollie')
        self.assertEqual(pangu.spacing('Vinta+陳上進'), u'Vinta + 陳上進')
        self.assertEqual(pangu.spacing('陳上進+Vinta'), u'陳上進 + Vinta')
        self.assertEqual(pangu.spacing('得到一個A+B的結果'), u'得到一個 A+B 的結果')
        self.assertEqual(pangu.spacing('得到一個C++的結果'), u'得到一個 C++ 的結果')

    def test_equal(self):
        self.assertEqual(pangu.spacing('前面=後面'), u'前面 = 後面')
        self.assertEqual(pangu.spacing('前面 = 後面'), u'前面 = 後面')
        self.assertEqual(pangu.spacing('Vinta=Mollie'), u'Vinta=Mollie')
        self.assertEqual(pangu.spacing('Vinta=陳上進'), u'Vinta = 陳上進')
        self.assertEqual(pangu.spacing('陳上進=Vinta'), u'陳上進 = Vinta')
        self.assertEqual(pangu.spacing('得到一個A=B的結果'), u'得到一個 A=B 的結果')

    def test_braces(self):
        self.assertEqual(pangu.spacing('前面{中文123漢字}後面'), u'前面 {中文 123 漢字} 後面')
        self.assertEqual(pangu.spacing('前面{中文123}後面'), u'前面 {中文 123} 後面')
        self.assertEqual(pangu.spacing('前面{123漢字}後面'), u'前面 {123 漢字} 後面')
        self.assertEqual(pangu.spacing('前面{中文123漢字} tail'), u'前面 {中文 123 漢字} tail')
        self.assertEqual(pangu.spacing('head {中文123漢字}後面'), u'head {中文 123 漢字} 後面')
        self.assertEqual(pangu.spacing('head {中文123漢字} tail'), u'head {中文 123 漢字} tail')

    def test_brackets(self):
        self.assertEqual(pangu.spacing('前面[中文123漢字]後面'), u'前面 [中文 123 漢字] 後面')
        self.assertEqual(pangu.spacing('前面[中文123]後面'), u'前面 [中文 123] 後面')
        self.assertEqual(pangu.spacing('前面[123漢字]後面'), u'前面 [123 漢字] 後面')
        self.assertEqual(pangu.spacing('前面[中文123漢字] tail'), u'前面 [中文 123 漢字] tail')
        self.assertEqual(pangu.spacing('head [中文123漢字]後面'), u'head [中文 123 漢字] 後面')
        self.assertEqual(pangu.spacing('head [中文123漢字] tail'), u'head [中文 123 漢字] tail')

    def test_pipe(self):
        self.assertEqual(pangu.spacing('前面|後面'), u'前面 | 後面')
        self.assertEqual(pangu.spacing('前面 | 後面'), u'前面 | 後面')
        self.assertEqual(pangu.spacing('Vinta|Mollie'), u'Vinta|Mollie')
        self.assertEqual(pangu.spacing('Vinta|陳上進'), u'Vinta | 陳上進')
        self.assertEqual(pangu.spacing('陳上進|Vinta'), u'陳上進 | Vinta')
        self.assertEqual(pangu.spacing('得到一個A|B的結果'), u'得到一個 A|B 的結果')

    def test_backslash(self):
        self.assertEqual(pangu.spacing('前面\後面'), u'前面 \ 後面')
        self.assertEqual(pangu.spacing('前面 \ 後面'), u'前面 \ 後面')

    def test_colon(self):
        self.assertEqual(pangu.spacing('前面:後面'), u'前面: 後面')
        self.assertEqual(pangu.spacing('前面 : 後面'), u'前面 : 後面')
        self.assertEqual(pangu.spacing('前面: 後面'), u'前面: 後面')

    def test_semicolon(self):
        self.assertEqual(pangu.spacing('前面;後面'), u'前面; 後面')
        self.assertEqual(pangu.spacing('前面 ; 後面'), u'前面 ; 後面')
        self.assertEqual(pangu.spacing('前面; 後面'), u'前面; 後面')

    def test_quote(self):
        self.assertEqual(pangu.spacing('前面"中文123漢字"後面'), u'前面 "中文 123 漢字" 後面')
        self.assertEqual(pangu.spacing('前面"中文123"後面'), u'前面 "中文 123" 後面')
        self.assertEqual(pangu.spacing('前面"123漢字"後面'), u'前面 "123 漢字" 後面')
        self.assertEqual(pangu.spacing('前面"中文123漢字" tail'), u'前面 "中文 123 漢字" tail')
        self.assertEqual(pangu.spacing('head "中文123漢字"後面'), u'head "中文 123 漢字" 後面')
        self.assertEqual(pangu.spacing('head "中文123漢字" tail'), u'head "中文 123 漢字" tail')

    def test_single_quote(self):
        self.assertEqual(u"前面 '中文 123 漢字' 後面", pangu.spacing("前面'中文123漢字'後面"))
        self.assertEqual(u"前面 '中文 123' 後面", pangu.spacing("前面'中文123'後面"))
        self.assertEqual(u"前面 '123 漢字' 後面", pangu.spacing("前面'123漢字'後面"))
        self.assertEqual(u"前面 '中文 123 漢字' tail", pangu.spacing("前面'中文123漢字' tail"))
        self.assertEqual(u"head '中文 123 漢字' 後面", pangu.spacing("head '中文123漢字'後面"))
        self.assertEqual(u"head '中文 123 漢字' tail", pangu.spacing("head '中文123漢字' tail"))
        self.assertEqual(u"陳上進 likes 林依諾's status.", pangu.spacing("陳上進 likes 林依諾's status."))

    def test_less_than_and_greater_than(self):
        self.assertEqual(pangu.spacing('前面<中文123漢字>後面'), u'前面 <中文 123 漢字> 後面')
        self.assertEqual(pangu.spacing('前面<中文123>後面'), u'前面 <中文 123> 後面')
        self.assertEqual(pangu.spacing('前面<123漢字>後面'), u'前面 <123 漢字> 後面')
        self.assertEqual(pangu.spacing('前面<中文123漢字> tail'), u'前面 <中文 123 漢字> tail')
        self.assertEqual(pangu.spacing('head <中文123漢字>後面'), u'head <中文 123 漢字> 後面')
        self.assertEqual(pangu.spacing('head <中文123漢字> tail'), u'head <中文 123 漢字> tail')

    def test_less_than(self):
        self.assertEqual(pangu.spacing('前面<後面'), u'前面 < 後面')
        self.assertEqual(pangu.spacing('前面 < 後面'), u'前面 < 後面')
        self.assertEqual(pangu.spacing('Vinta<Mollie'), u'Vinta<Mollie')
        self.assertEqual(pangu.spacing('Vinta<陳上進'), u'Vinta < 陳上進')
        self.assertEqual(pangu.spacing('陳上進<Vinta'), u'陳上進 < Vinta')
        self.assertEqual(pangu.spacing('得到一個A<B的結果'), u'得到一個 A<B 的結果')

    def test_comma(self):
        self.assertEqual(pangu.spacing('前面,後面'), u'前面, 後面')
        self.assertEqual(pangu.spacing('前面 , 後面'), u'前面 , 後面')
        self.assertEqual(pangu.spacing('前面, 後面'), u'前面, 後面')

    def test_greater_than(self):
        self.assertEqual(pangu.spacing('前面>後面'), u'前面 > 後面')
        self.assertEqual(pangu.spacing('前面 > 後面'), u'前面 > 後面')
        self.assertEqual(pangu.spacing('Vinta>Mollie'), u'Vinta>Mollie')
        self.assertEqual(pangu.spacing('Vinta>陳上進'), u'Vinta > 陳上進')
        self.assertEqual(pangu.spacing('陳上進>Vinta'), u'陳上進 > Vinta')
        self.assertEqual(pangu.spacing('得到一個A>B的結果'), u'得到一個 A>B 的結果')

    def test_period(self):
        self.assertEqual(pangu.spacing('前面.後面'), u'前面. 後面')
        self.assertEqual(pangu.spacing('前面 . 後面'), u'前面 . 後面')
        self.assertEqual(pangu.spacing('前面. 後面'), u'前面. 後面')

    def test_question_mark(self):
        self.assertEqual(pangu.spacing('前面?後面'), u'前面? 後面')
        self.assertEqual(pangu.spacing('前面 ? 後面'), u'前面 ? 後面')
        self.assertEqual(pangu.spacing('前面? 後面'), u'前面? 後面')

    def test_slash(self):
        self.assertEqual(pangu.spacing('前面/後面'), u'前面 / 後面')
        self.assertEqual(pangu.spacing('前面 / 後面'), u'前面 / 後面')
        self.assertEqual(pangu.spacing('Vinta/Mollie'), u'Vinta/Mollie')
        self.assertEqual(pangu.spacing('Vinta/陳上進'), u'Vinta / 陳上進')
        self.assertEqual(pangu.spacing('陳上進/Vinta'), u'陳上進 / Vinta')
        self.assertEqual(pangu.spacing('得到一個A/B的結果'), u'得到一個 A/B 的結果')

    def test_special_characters(self):
        # \u201c and \u201d
        self.assertEqual(pangu.spacing('前面“中文123漢字”後面'), u'前面 “中文 123 漢字” 後面')

        # \u2026
        self.assertEqual(pangu.spacing('前面…後面'), u'前面… 後面')
        self.assertEqual(pangu.spacing('前面……後面'), u'前面…… 後面')

        # \u2027
        self.assertEqual(pangu.spacing('前面‧後面'), u'前面 ‧ 後面')


if __name__ == '__main__':
    unittest.main()
