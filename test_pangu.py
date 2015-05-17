# coding: utf-8

from __future__ import unicode_literals
import unittest

import pangu


class PanguTestCase(unittest.TestCase):

    def test_spacing(self):
        self.assertEqual('新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾', pangu.spacing('新八的構造成分有95%是眼鏡、3%是水、2%是垃圾'))
        self.assertEqual('所以, 請問 Jackey 的鼻子有幾個? 3.14 個!', pangu.spacing('所以,請問Jackey的鼻子有幾個?3.14個!'))

    def test_tilde(self):
        self.assertEqual('前面~ 後面', pangu.spacing('前面~後面'))
        self.assertEqual('前面 ~ 後面', pangu.spacing('前面 ~ 後面'))
        self.assertEqual('前面~ 後面', pangu.spacing('前面~ 後面'))

    def test_back_quote(self):
        self.assertEqual('前面 ` 後面', pangu.spacing('前面`後面'))
        self.assertEqual('前面 ` 後面', pangu.spacing('前面 ` 後面'))
        self.assertEqual('前面 ` 後面', pangu.spacing('前面` 後面'))

    def test_exclamation_mark(self):
        self.assertEqual('前面! 後面', pangu.spacing('前面!後面'))
        self.assertEqual('前面 ! 後面', pangu.spacing('前面 ! 後面'))
        self.assertEqual('前面! 後面', pangu.spacing('前面! 後面'))

    def test_at(self):
        # https://twitter.com/vinta
        self.assertEqual('前面 @vinta 後面', pangu.spacing('前面@vinta後面'))
        self.assertEqual('前面 @vinta 後面', pangu.spacing('前面 @vinta 後面'))

        # http://weibo.com/vintalines
        self.assertEqual('前面 @陳上進 後面', pangu.spacing('前面@陳上進 後面'))
        self.assertEqual('前面 @陳上進 後面', pangu.spacing('前面 @陳上進 後面'))
        self.assertEqual('前面 @陳上進 tail', pangu.spacing('前面 @陳上進tail'))

    def test_hash(self):
        self.assertEqual('前面 #H2G2 後面', pangu.spacing('前面#H2G2後面'))
        self.assertEqual('前面 #銀河便車指南 後面', pangu.spacing('前面#銀河便車指南 後面'))
        self.assertEqual('前面 #銀河便車指南 tail', pangu.spacing('前面#銀河便車指南tail'))
        self.assertEqual('前面 #銀河公車指南 #銀河拖吊車指南 後面', pangu.spacing('前面#銀河公車指南 #銀河拖吊車指南 後面'))

        self.assertEqual('前面 #H2G2# 後面', pangu.spacing('前面#H2G2#後面'))
        self.assertEqual('前面 #銀河閃電霹靂車指南# 後面', pangu.spacing('前面#銀河閃電霹靂車指南#後面'))

    def test_dollar(self):
        self.assertEqual('前面 $ 後面', pangu.spacing('前面$後面'))
        self.assertEqual('前面 $ 後面', pangu.spacing('前面 $ 後面'))

        self.assertEqual('前面 $100 後面', pangu.spacing('前面$100後面'))

    def test_percent(self):
        self.assertEqual('前面 % 後面', pangu.spacing('前面%後面'))
        self.assertEqual('前面 % 後面', pangu.spacing('前面 % 後面'))

        self.assertEqual('前面 100% 後面', pangu.spacing('前面100%後面'))

    def test_caret(self):
        self.assertEqual('前面 ^ 後面', pangu.spacing('前面^後面'))
        self.assertEqual('前面 ^ 後面', pangu.spacing('前面 ^ 後面'))

    def test_ampersand(self):
        self.assertEqual('前面 & 後面', pangu.spacing('前面&後面'))
        self.assertEqual('前面 & 後面', pangu.spacing('前面 & 後面'))

        self.assertEqual('Vinta&Mollie', pangu.spacing('Vinta&Mollie'))
        self.assertEqual('Vinta & 陳上進', pangu.spacing('Vinta&陳上進'))
        self.assertEqual('陳上進 & Vinta', pangu.spacing('陳上進&Vinta'))

        self.assertEqual('得到一個 A&B 的結果', pangu.spacing('得到一個A&B的結果'))

    def test_asterisk(self):
        self.assertEqual('前面 * 後面', pangu.spacing('前面*後面'))
        self.assertEqual('前面 * 後面', pangu.spacing('前面 * 後面'))

        self.assertEqual('Vinta*Mollie', pangu.spacing('Vinta*Mollie'))
        self.assertEqual('Vinta * 陳上進', pangu.spacing('Vinta*陳上進'))
        self.assertEqual('陳上進 * Vinta', pangu.spacing('陳上進*Vinta'))

        self.assertEqual('得到一個 A*B 的結果', pangu.spacing('得到一個A*B的結果'))

    def test_parenthese_1(self):
        self.assertEqual('前面 (中文 123 漢字) 後面', pangu.spacing('前面(中文123漢字)後面'))
        self.assertEqual('前面 (中文 123) 後面', pangu.spacing('前面(中文123)後面'))
        self.assertEqual('前面 (123 漢字) 後面', pangu.spacing('前面(123漢字)後面'))
        self.assertEqual('前面 (中文 123 漢字) tail', pangu.spacing('前面(中文123漢字) tail'))
        self.assertEqual('head (中文 123 漢字) 後面', pangu.spacing('head (中文123漢字)後面'))
        self.assertEqual('head (中文 123 漢字) tail', pangu.spacing('head (中文123漢字) tail'))

    def test_minus(self):
        self.assertEqual('前面 - 後面', pangu.spacing('前面-後面'))
        self.assertEqual('前面 - 後面', pangu.spacing('前面 - 後面'))

        self.assertEqual('Vinta-Mollie', pangu.spacing('Vinta-Mollie'))
        self.assertEqual('Vinta - 陳上進', pangu.spacing('Vinta-陳上進'))
        self.assertEqual('陳上進 - Vinta', pangu.spacing('陳上進-Vinta'))

        self.assertEqual('得到一個 A-B 的結果', pangu.spacing('得到一個A-B的結果'))

    def test_underscore(self):
        self.assertEqual('前面_後面', pangu.spacing('前面_後面'))
        self.assertEqual('前面 _ 後面', pangu.spacing('前面 _ 後面'))

    def test_plus(self):
        self.assertEqual('前面 + 後面', pangu.spacing('前面+後面'))
        self.assertEqual('前面 + 後面', pangu.spacing('前面 + 後面'))

        self.assertEqual('Vinta+Mollie', pangu.spacing('Vinta+Mollie'))
        self.assertEqual('Vinta + 陳上進', pangu.spacing('Vinta+陳上進'))
        self.assertEqual('陳上進 + Vinta', pangu.spacing('陳上進+Vinta'))

        self.assertEqual('得到一個 A+B 的結果', pangu.spacing('得到一個A+B的結果'))

        self.assertEqual('得到一個 C++ 的結果', pangu.spacing('得到一個C++的結果'))

    def test_equal(self):
        self.assertEqual('前面 = 後面', pangu.spacing('前面=後面'))
        self.assertEqual('前面 = 後面', pangu.spacing('前面 = 後面'))

        self.assertEqual('Vinta=Mollie', pangu.spacing('Vinta=Mollie'))
        self.assertEqual('Vinta = 陳上進', pangu.spacing('Vinta=陳上進'))
        self.assertEqual('陳上進 = Vinta', pangu.spacing('陳上進=Vinta'))

        self.assertEqual('得到一個 A=B 的結果', pangu.spacing('得到一個A=B的結果'))

    def test_brace(self):
        self.assertEqual('前面 {中文 123 漢字} 後面', pangu.spacing('前面{中文123漢字}後面'))
        self.assertEqual('前面 {中文 123} 後面', pangu.spacing('前面{中文123}後面'))
        self.assertEqual('前面 {123 漢字} 後面', pangu.spacing('前面{123漢字}後面'))
        self.assertEqual('前面 {中文 123 漢字} tail', pangu.spacing('前面{中文123漢字} tail'))
        self.assertEqual('head {中文 123 漢字} 後面', pangu.spacing('head {中文123漢字}後面'))
        self.assertEqual('head {中文 123 漢字} tail', pangu.spacing('head {中文123漢字} tail'))

    def test_bracket(self):
        self.assertEqual('前面 [中文 123 漢字] 後面', pangu.spacing('前面[中文123漢字]後面'))
        self.assertEqual('前面 [中文 123] 後面', pangu.spacing('前面[中文123]後面'))
        self.assertEqual('前面 [123 漢字] 後面', pangu.spacing('前面[123漢字]後面'))
        self.assertEqual('前面 [中文 123 漢字] tail', pangu.spacing('前面[中文123漢字] tail'))
        self.assertEqual('head [中文 123 漢字] 後面', pangu.spacing('head [中文123漢字]後面'))
        self.assertEqual('head [中文 123 漢字] tail', pangu.spacing('head [中文123漢字] tail'))

    def test_pipe(self):
        self.assertEqual('前面 | 後面', pangu.spacing('前面|後面'))
        self.assertEqual('前面 | 後面', pangu.spacing('前面 | 後面'))

        self.assertEqual('Vinta|Mollie', pangu.spacing('Vinta|Mollie'))
        self.assertEqual('Vinta | 陳上進', pangu.spacing('Vinta|陳上進'))
        self.assertEqual('陳上進 | Vinta', pangu.spacing('陳上進|Vinta'))

        self.assertEqual('得到一個 A|B 的結果', pangu.spacing('得到一個A|B的結果'))

    def test_backslash(self):
        self.assertEqual('前面 \ 後面', pangu.spacing('前面\後面'))

    def test_colon(self):
        self.assertEqual('前面: 後面', pangu.spacing('前面:後面'))
        self.assertEqual('前面 : 後面', pangu.spacing('前面 : 後面'))
        self.assertEqual('前面: 後面', pangu.spacing('前面: 後面'))

    def test_semicolon(self):
        self.assertEqual('前面; 後面', pangu.spacing('前面;後面'))
        self.assertEqual('前面 ; 後面', pangu.spacing('前面 ; 後面'))
        self.assertEqual('前面; 後面', pangu.spacing('前面; 後面'))

    def test_quote(self):
        self.assertEqual('前面 "中文 123 漢字" 後面', pangu.spacing('前面"中文123漢字"後面'))
        self.assertEqual('前面 "中文 123" 後面', pangu.spacing('前面"中文123"後面'))
        self.assertEqual('前面 "123 漢字" 後面', pangu.spacing('前面"123漢字"後面'))
        self.assertEqual('前面 "中文 123 漢字" tail', pangu.spacing('前面"中文123漢字" tail'))
        self.assertEqual('head "中文 123 漢字" 後面', pangu.spacing('head "中文123漢字"後面'))
        self.assertEqual('head "中文 123 漢字" tail', pangu.spacing('head "中文123漢字" tail'))

        # \u201c and \u201d
        self.assertEqual('前面 “中文 123 漢字” 後面', pangu.spacing('前面“中文123漢字”後面'))

    def test_single_quote(self):
        self.assertEqual("前面 '中文 123 漢字' 後面", pangu.spacing("前面'中文123漢字'後面"))
        self.assertEqual("前面 '中文 123' 後面", pangu.spacing("前面'中文123'後面"))
        self.assertEqual("前面 '123 漢字' 後面", pangu.spacing("前面'123漢字'後面"))
        self.assertEqual("前面 '中文 123 漢字' tail", pangu.spacing("前面'中文123漢字' tail"))
        self.assertEqual("head '中文 123 漢字' 後面", pangu.spacing("head '中文123漢字'後面"))
        self.assertEqual("head '中文 123 漢字' tail", pangu.spacing("head '中文123漢字' tail"))

        self.assertEqual("陳上進 likes 林依諾's status.", pangu.spacing("陳上進 likes 林依諾's status."))

    def test_less_than(self):
        self.assertEqual('前面 < 後面', pangu.spacing('前面<後面'))
        self.assertEqual('前面 < 後面', pangu.spacing('前面 < 後面'))

        self.assertEqual('Vinta<Mollie', pangu.spacing('Vinta<Mollie'))
        self.assertEqual('Vinta < 陳上進', pangu.spacing('Vinta<陳上進'))
        self.assertEqual('陳上進 < Vinta', pangu.spacing('陳上進<Vinta'))

        self.assertEqual('得到一個 A<B 的結果', pangu.spacing('得到一個A<B的結果'))

        self.assertEqual('前面 <中文 123 漢字> 後面', pangu.spacing('前面<中文123漢字>後面'))
        self.assertEqual('前面 <中文 123> 後面', pangu.spacing('前面<中文123>後面'))
        self.assertEqual('前面 <123 漢字> 後面', pangu.spacing('前面<123漢字>後面'))
        self.assertEqual('前面 <中文 123 漢字> tail', pangu.spacing('前面<中文123漢字> tail'))
        self.assertEqual('head <中文 123 漢字> 後面', pangu.spacing('head <中文123漢字>後面'))
        self.assertEqual('head <中文 123 漢字> tail', pangu.spacing('head <中文123漢字> tail'))

    def test_comma(self):
        self.assertEqual('前面, 後面', pangu.spacing('前面,後面'))
        self.assertEqual('前面 , 後面', pangu.spacing('前面 , 後面'))
        self.assertEqual('前面, 後面', pangu.spacing('前面, 後面'))

    def test_greater_than(self):
        self.assertEqual('前面 > 後面', pangu.spacing('前面>後面'))
        self.assertEqual('前面 > 後面', pangu.spacing('前面 > 後面'))

        self.assertEqual('Vinta>Mollie', pangu.spacing('Vinta>Mollie'))
        self.assertEqual('Vinta > 陳上進', pangu.spacing('Vinta>陳上進'))
        self.assertEqual('陳上進 > Vinta', pangu.spacing('陳上進>Vinta'))

        self.assertEqual('得到一個 A>B 的結果', pangu.spacing('得到一個A>B的結果'))

    def test_period(self):
        self.assertEqual('前面. 後面', pangu.spacing('前面.後面'))
        self.assertEqual('前面 . 後面', pangu.spacing('前面 . 後面'))
        self.assertEqual('前面. 後面', pangu.spacing('前面. 後面'))

        # … is \u2026
        self.assertEqual('前面… 後面', pangu.spacing('前面…後面'))
        self.assertEqual('前面…… 後面', pangu.spacing('前面……後面'))

    def test_question_mark(self):
        self.assertEqual('前面? 後面', pangu.spacing('前面?後面'))
        self.assertEqual('前面 ? 後面', pangu.spacing('前面 ? 後面'))
        self.assertEqual('前面? 後面', pangu.spacing('前面? 後面'))

    def test_slash(self):
        self.assertEqual('前面 / 後面', pangu.spacing('前面/後面'))
        self.assertEqual('前面 / 後面', pangu.spacing('前面 / 後面'))

        self.assertEqual('Vinta/Mollie', pangu.spacing('Vinta/Mollie'))
        self.assertEqual('Vinta / 陳上進', pangu.spacing('Vinta/陳上進'))
        self.assertEqual('陳上進 / Vinta', pangu.spacing('陳上進/Vinta'))

        self.assertEqual('得到一個 A/B 的結果', pangu.spacing('得到一個A/B的結果'))


if __name__ == '__main__':
    unittest.main()
