# coding: utf-8

# from __future__ import unicode_literals
import unittest

import pangu


class PanguTestCase(unittest.TestCase):

    def test_text_spacing(self):
        self.assertEqual(u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾', pangu.text_spacing('新八的構造成分有95%是眼鏡、3%是水、2%是垃圾'))
        self.assertEqual(u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾', pangu.text_spacing(u'新八的構造成分有95%是眼鏡、3%是水、2%是垃圾'))

        self.assertEqual(u'所以, 請問 Jackey 的鼻子有幾個? 3.14 個!', pangu.text_spacing('所以,請問Jackey的鼻子有幾個?3.14個!'))
        self.assertEqual(u'所以, 請問 Jackey 的鼻子有幾個? 3.14 個!', pangu.text_spacing(u'所以,請問Jackey的鼻子有幾個?3.14個!'))

        self.assertEqual(u'JUST WE 就是 JUST WE，既不偉大也不卑微！', pangu.text_spacing('JUST WE就是JUST WE，既不偉大也不卑微！'))
        self.assertEqual(u'JUST WE 就是 JUST WE，既不偉大也不卑微！', pangu.text_spacing(u'JUST WE就是JUST WE，既不偉大也不卑微！'))

        self.assertEqual(u'搭載 MP3 播放器，連續播放時數最長達到 124 小時的超強利刃…… 菊一文字 RX-7!', pangu.text_spacing('搭載MP3播放器，連續播放時數最長達到124小時的超強利刃……菊一文字RX-7!'))
        self.assertEqual(u'搭載 MP3 播放器，連續播放時數最長達到 124 小時的超強利刃…… 菊一文字 RX-7!', pangu.text_spacing(u'搭載MP3播放器，連續播放時數最長達到124小時的超強利刃……菊一文字RX-7!'))

    def test_text_spacing_too_short(self):
        self.assertEqual(u'V', pangu.spacing('V'))

    def test_tilde(self):
        self.assertEqual(u'前面~ 後面', pangu.text_spacing('前面~後面'))
        self.assertEqual(u'前面 ~ 後面', pangu.text_spacing('前面 ~ 後面'))
        self.assertEqual(u'前面~ 後面', pangu.text_spacing('前面~ 後面'))

    def test_back_quote(self):
        self.assertEqual(u'前面 ` 後面', pangu.text_spacing('前面`後面'))
        self.assertEqual(u'前面 ` 後面', pangu.text_spacing('前面 ` 後面'))
        self.assertEqual(u'前面 ` 後面', pangu.text_spacing('前面` 後面'))

    def test_exclamation_mark(self):
        self.assertEqual(u'前面! 後面', pangu.text_spacing('前面!後面'))
        self.assertEqual(u'前面 ! 後面', pangu.text_spacing('前面 ! 後面'))
        self.assertEqual(u'前面! 後面', pangu.text_spacing('前面! 後面'))

    def test_at(self):
        # https://twitter.com/vinta
        self.assertEqual(u'前面 @vinta 後面', pangu.text_spacing('前面@vinta後面'))
        self.assertEqual(u'前面 @vinta 後面', pangu.text_spacing('前面 @vinta 後面'))

        # http://weibo.com/vintalines
        self.assertEqual(u'前面 @陳上進 後面', pangu.text_spacing('前面@陳上進 後面'))
        self.assertEqual(u'前面 @陳上進 後面', pangu.text_spacing('前面 @陳上進 後面'))
        self.assertEqual(u'前面 @陳上進 tail', pangu.text_spacing('前面 @陳上進tail'))

    def test_hash(self):
        self.assertEqual(u'前面 #H2G2 後面', pangu.text_spacing('前面#H2G2後面'))
        self.assertEqual(u'前面 #銀河便車指南 後面', pangu.text_spacing('前面#銀河便車指南 後面'))
        self.assertEqual(u'前面 #銀河便車指南 tail', pangu.text_spacing('前面#銀河便車指南tail'))
        self.assertEqual(u'前面 #銀河公車指南 #銀河拖吊車指南 後面', pangu.text_spacing('前面#銀河公車指南 #銀河拖吊車指南 後面'))

        self.assertEqual(u'前面 #H2G2# 後面', pangu.text_spacing('前面#H2G2#後面'))
        self.assertEqual(u'前面 #銀河閃電霹靂車指南# 後面', pangu.text_spacing('前面#銀河閃電霹靂車指南#後面'))

    def test_dollar(self):
        self.assertEqual(u'前面 $ 後面', pangu.text_spacing('前面$後面'))
        self.assertEqual(u'前面 $ 後面', pangu.text_spacing('前面 $ 後面'))

        self.assertEqual(u'前面 $100 後面', pangu.text_spacing('前面$100後面'))

    def test_percent(self):
        self.assertEqual(u'前面 % 後面', pangu.text_spacing('前面%後面'))
        self.assertEqual(u'前面 % 後面', pangu.text_spacing('前面 % 後面'))

        self.assertEqual(u'前面 100% 後面', pangu.text_spacing('前面100%後面'))

    def test_caret(self):
        self.assertEqual(u'前面 ^ 後面', pangu.text_spacing('前面^後面'))
        self.assertEqual(u'前面 ^ 後面', pangu.text_spacing('前面 ^ 後面'))

    def test_ampersand(self):
        self.assertEqual(u'前面 & 後面', pangu.text_spacing('前面&後面'))
        self.assertEqual(u'前面 & 後面', pangu.text_spacing('前面 & 後面'))

        self.assertEqual(u'Vinta&Mollie', pangu.text_spacing('Vinta&Mollie'))
        self.assertEqual(u'Vinta & 陳上進', pangu.text_spacing('Vinta&陳上進'))
        self.assertEqual(u'陳上進 & Vinta', pangu.text_spacing('陳上進&Vinta'))

        self.assertEqual(u'得到一個 A&B 的結果', pangu.text_spacing('得到一個A&B的結果'))

    def test_asterisk(self):
        self.assertEqual(u'前面 * 後面', pangu.text_spacing('前面*後面'))
        self.assertEqual(u'前面 * 後面', pangu.text_spacing('前面 * 後面'))

        self.assertEqual(u'Vinta*Mollie', pangu.text_spacing('Vinta*Mollie'))
        self.assertEqual(u'Vinta * 陳上進', pangu.text_spacing('Vinta*陳上進'))
        self.assertEqual(u'陳上進 * Vinta', pangu.text_spacing('陳上進*Vinta'))

        self.assertEqual(u'得到一個 A*B 的結果', pangu.text_spacing('得到一個A*B的結果'))

    def test_parenthese_1(self):
        self.assertEqual(u'前面 (中文 123 漢字) 後面', pangu.text_spacing('前面(中文123漢字)後面'))
        self.assertEqual(u'前面 (中文 123) 後面', pangu.text_spacing('前面(中文123)後面'))
        self.assertEqual(u'前面 (123 漢字) 後面', pangu.text_spacing('前面(123漢字)後面'))
        self.assertEqual(u'前面 (中文 123 漢字) tail', pangu.text_spacing('前面(中文123漢字) tail'))
        self.assertEqual(u'head (中文 123 漢字) 後面', pangu.text_spacing('head (中文123漢字)後面'))
        self.assertEqual(u'head (中文 123 漢字) tail', pangu.text_spacing('head (中文123漢字) tail'))

    def test_minus(self):
        self.assertEqual(u'前面 - 後面', pangu.text_spacing('前面-後面'))
        self.assertEqual(u'前面 - 後面', pangu.text_spacing('前面 - 後面'))

        self.assertEqual(u'Vinta-Mollie', pangu.text_spacing('Vinta-Mollie'))
        self.assertEqual(u'Vinta - 陳上進', pangu.text_spacing('Vinta-陳上進'))
        self.assertEqual(u'陳上進 - Vinta', pangu.text_spacing('陳上進-Vinta'))

        self.assertEqual(u'得到一個 A-B 的結果', pangu.text_spacing('得到一個A-B的結果'))

    def test_underscore(self):
        self.assertEqual(u'前面_後面', pangu.text_spacing('前面_後面'))
        self.assertEqual(u'前面 _ 後面', pangu.text_spacing('前面 _ 後面'))

    def test_plus(self):
        self.assertEqual(u'前面 + 後面', pangu.text_spacing('前面+後面'))
        self.assertEqual(u'前面 + 後面', pangu.text_spacing('前面 + 後面'))

        self.assertEqual(u'Vinta+Mollie', pangu.text_spacing('Vinta+Mollie'))
        self.assertEqual(u'Vinta + 陳上進', pangu.text_spacing('Vinta+陳上進'))
        self.assertEqual(u'陳上進 + Vinta', pangu.text_spacing('陳上進+Vinta'))

        self.assertEqual(u'得到一個 A+B 的結果', pangu.text_spacing('得到一個A+B的結果'))

        self.assertEqual(u'得到一個 C++ 的結果', pangu.text_spacing('得到一個C++的結果'))

    def test_equal(self):
        self.assertEqual(u'前面 = 後面', pangu.text_spacing('前面=後面'))
        self.assertEqual(u'前面 = 後面', pangu.text_spacing('前面 = 後面'))

        self.assertEqual(u'Vinta=Mollie', pangu.text_spacing('Vinta=Mollie'))
        self.assertEqual(u'Vinta = 陳上進', pangu.text_spacing('Vinta=陳上進'))
        self.assertEqual(u'陳上進 = Vinta', pangu.text_spacing('陳上進=Vinta'))

        self.assertEqual(u'得到一個 A=B 的結果', pangu.text_spacing('得到一個A=B的結果'))

    def test_brace(self):
        self.assertEqual(u'前面 {中文 123 漢字} 後面', pangu.text_spacing('前面{中文123漢字}後面'))
        self.assertEqual(u'前面 {中文 123} 後面', pangu.text_spacing('前面{中文123}後面'))
        self.assertEqual(u'前面 {123 漢字} 後面', pangu.text_spacing('前面{123漢字}後面'))
        self.assertEqual(u'前面 {中文 123 漢字} tail', pangu.text_spacing('前面{中文123漢字} tail'))
        self.assertEqual(u'head {中文 123 漢字} 後面', pangu.text_spacing('head {中文123漢字}後面'))
        self.assertEqual(u'head {中文 123 漢字} tail', pangu.text_spacing('head {中文123漢字} tail'))

    def test_bracket(self):
        self.assertEqual(u'前面 [中文 123 漢字] 後面', pangu.text_spacing('前面[中文123漢字]後面'))
        self.assertEqual(u'前面 [中文 123] 後面', pangu.text_spacing('前面[中文123]後面'))
        self.assertEqual(u'前面 [123 漢字] 後面', pangu.text_spacing('前面[123漢字]後面'))
        self.assertEqual(u'前面 [中文 123 漢字] tail', pangu.text_spacing('前面[中文123漢字] tail'))
        self.assertEqual(u'head [中文 123 漢字] 後面', pangu.text_spacing('head [中文123漢字]後面'))
        self.assertEqual(u'head [中文 123 漢字] tail', pangu.text_spacing('head [中文123漢字] tail'))

    def test_pipe(self):
        self.assertEqual(u'前面 | 後面', pangu.text_spacing('前面|後面'))
        self.assertEqual(u'前面 | 後面', pangu.text_spacing('前面 | 後面'))

        self.assertEqual(u'Vinta|Mollie', pangu.text_spacing('Vinta|Mollie'))
        self.assertEqual(u'Vinta | 陳上進', pangu.text_spacing('Vinta|陳上進'))
        self.assertEqual(u'陳上進 | Vinta', pangu.text_spacing('陳上進|Vinta'))

        self.assertEqual(u'得到一個 A|B 的結果', pangu.text_spacing('得到一個A|B的結果'))

    def test_backslash(self):
        self.assertEqual(u'前面 \ 後面', pangu.text_spacing('前面\後面'))

    def test_colon(self):
        self.assertEqual(u'前面: 後面', pangu.text_spacing('前面:後面'))
        self.assertEqual(u'前面 : 後面', pangu.text_spacing('前面 : 後面'))
        self.assertEqual(u'前面: 後面', pangu.text_spacing('前面: 後面'))

    def test_semicolon(self):
        self.assertEqual(u'前面; 後面', pangu.text_spacing('前面;後面'))
        self.assertEqual(u'前面 ; 後面', pangu.text_spacing('前面 ; 後面'))
        self.assertEqual(u'前面; 後面', pangu.text_spacing('前面; 後面'))

    def test_quote(self):
        self.assertEqual(u'前面 "中文 123 漢字" 後面', pangu.text_spacing('前面"中文123漢字"後面'))
        self.assertEqual(u'前面 "中文 123" 後面', pangu.text_spacing('前面"中文123"後面'))
        self.assertEqual(u'前面 "123 漢字" 後面', pangu.text_spacing('前面"123漢字"後面'))
        self.assertEqual(u'前面 "中文 123 漢字" tail', pangu.text_spacing('前面"中文123漢字" tail'))
        self.assertEqual(u'head "中文 123 漢字" 後面', pangu.text_spacing('head "中文123漢字"後面'))
        self.assertEqual(u'head "中文 123 漢字" tail', pangu.text_spacing('head "中文123漢字" tail'))

        # \u201c and \u201d
        self.assertEqual(u'前面 “中文 123 漢字” 後面', pangu.text_spacing('前面“中文123漢字”後面'))

    def test_single_quote(self):
        self.assertEqual(u"前面 '中文 123 漢字' 後面", pangu.text_spacing("前面'中文123漢字'後面"))
        self.assertEqual(u"前面 '中文 123' 後面", pangu.text_spacing("前面'中文123'後面"))
        self.assertEqual(u"前面 '123 漢字' 後面", pangu.text_spacing("前面'123漢字'後面"))
        self.assertEqual(u"前面 '中文 123 漢字' tail", pangu.text_spacing("前面'中文123漢字' tail"))
        self.assertEqual(u"head '中文 123 漢字' 後面", pangu.text_spacing("head '中文123漢字'後面"))
        self.assertEqual(u"head '中文 123 漢字' tail", pangu.text_spacing("head '中文123漢字' tail"))

        self.assertEqual(u"陳上進 likes 林依諾's status.", pangu.text_spacing("陳上進 likes 林依諾's status."))

    def test_less_than(self):
        self.assertEqual(u'前面 < 後面', pangu.text_spacing('前面<後面'))
        self.assertEqual(u'前面 < 後面', pangu.text_spacing('前面 < 後面'))

        self.assertEqual(u'Vinta<Mollie', pangu.text_spacing('Vinta<Mollie'))
        self.assertEqual(u'Vinta < 陳上進', pangu.text_spacing('Vinta<陳上進'))
        self.assertEqual(u'陳上進 < Vinta', pangu.text_spacing('陳上進<Vinta'))

        self.assertEqual(u'得到一個 A<B 的結果', pangu.text_spacing('得到一個A<B的結果'))

        self.assertEqual(u'前面 <中文 123 漢字> 後面', pangu.text_spacing('前面<中文123漢字>後面'))
        self.assertEqual(u'前面 <中文 123> 後面', pangu.text_spacing('前面<中文123>後面'))
        self.assertEqual(u'前面 <123 漢字> 後面', pangu.text_spacing('前面<123漢字>後面'))
        self.assertEqual(u'前面 <中文 123 漢字> tail', pangu.text_spacing('前面<中文123漢字> tail'))
        self.assertEqual(u'head <中文 123 漢字> 後面', pangu.text_spacing('head <中文123漢字>後面'))
        self.assertEqual(u'head <中文 123 漢字> tail', pangu.text_spacing('head <中文123漢字> tail'))

    def test_comma(self):
        self.assertEqual(u'前面, 後面', pangu.text_spacing('前面,後面'))
        self.assertEqual(u'前面 , 後面', pangu.text_spacing('前面 , 後面'))
        self.assertEqual(u'前面, 後面', pangu.text_spacing('前面, 後面'))

    def test_greater_than(self):
        self.assertEqual(u'前面 > 後面', pangu.text_spacing('前面>後面'))
        self.assertEqual(u'前面 > 後面', pangu.text_spacing('前面 > 後面'))

        self.assertEqual(u'Vinta>Mollie', pangu.text_spacing('Vinta>Mollie'))
        self.assertEqual(u'Vinta > 陳上進', pangu.text_spacing('Vinta>陳上進'))
        self.assertEqual(u'陳上進 > Vinta', pangu.text_spacing('陳上進>Vinta'))

        self.assertEqual(u'得到一個 A>B 的結果', pangu.text_spacing('得到一個A>B的結果'))

    def test_period(self):
        self.assertEqual(u'前面. 後面', pangu.text_spacing('前面.後面'))
        self.assertEqual(u'前面 . 後面', pangu.text_spacing('前面 . 後面'))
        self.assertEqual(u'前面. 後面', pangu.text_spacing('前面. 後面'))

        # … is \u2026
        self.assertEqual(u'前面… 後面', pangu.text_spacing('前面…後面'))
        self.assertEqual(u'前面…… 後面', pangu.text_spacing('前面……後面'))

    def test_question_mark(self):
        self.assertEqual(u'前面? 後面', pangu.text_spacing('前面?後面'))
        self.assertEqual(u'前面 ? 後面', pangu.text_spacing('前面 ? 後面'))
        self.assertEqual(u'前面? 後面', pangu.text_spacing('前面? 後面'))

    def test_slash(self):
        self.assertEqual(u'前面 / 後面', pangu.text_spacing('前面/後面'))
        self.assertEqual(u'前面 / 後面', pangu.text_spacing('前面 / 後面'))

        self.assertEqual(u'Vinta/Mollie', pangu.text_spacing('Vinta/Mollie'))
        self.assertEqual(u'Vinta / 陳上進', pangu.text_spacing('Vinta/陳上進'))
        self.assertEqual(u'陳上進 / Vinta', pangu.text_spacing('陳上進/Vinta'))

        self.assertEqual(u'得到一個 A/B 的結果', pangu.text_spacing('得到一個A/B的結果'))


if __name__ == '__main__':
    unittest.main()
