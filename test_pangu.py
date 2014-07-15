# coding: utf-8
from __future__ import unicode_literals

import unittest

import pangu


class PanguTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_text_1(self):
        new_text = pangu.spacing('請問Jackie的鼻子有幾個？123個！')
        self.assertEqual(new_text, '請問 Jackie 的鼻子有幾個？123 個！')

        new_text = pangu.spacing('請問 Jackie 的鼻子有幾個？123 個！')
        self.assertEqual(new_text, '請問 Jackie 的鼻子有幾個？123 個！')

    def test_underscore(self):
        new_text = pangu.spacing('前面_後面')
        self.assertEqual(new_text, '前面_後面')

        new_text = pangu.spacing('前面 _ 後面')
        self.assertEqual(new_text, '前面 _ 後面')

    def test_tilde(self):
        new_text = pangu.spacing('前面~後面')
        self.assertEqual(new_text, '前面~ 後面')

        new_text = pangu.spacing('前面 ~ 後面')
        self.assertEqual(new_text, '前面 ~ 後面')

    def test_exclamation_mark(self):
        new_text = pangu.spacing('前面!後面')
        self.assertEqual(new_text, '前面! 後面')

    def test_question_mark(self):
        new_text = pangu.spacing('前面?後面')
        self.assertEqual(new_text, '前面? 後面')

    def test_colon(self):
        new_text = pangu.spacing('前面:後面')
        self.assertEqual(new_text, '前面: 後面')

    def test_semicolon(self):
        new_text = pangu.spacing('前面;後面')
        self.assertEqual(new_text, '前面; 後面')

    def test_comma(self):
        new_text = pangu.spacing('前面,後面')
        self.assertEqual(new_text, '前面, 後面')

    def test_period(self):
        new_text = pangu.spacing('前面.後面')
        self.assertEqual(new_text, '前面. 後面')

    def test_at_1(self):
        new_text = pangu.spacing('請@vinta吃大便')
        self.assertEqual(new_text, '請 @vinta 吃大便')

    def test_at_2(self):
        new_text = pangu.spacing('請@陳上進 吃大便')
        self.assertEqual(new_text, '請 @陳上進 吃大便')

    def test_hash_1(self):
        new_text = pangu.spacing('前面#H2G2後面')
        self.assertEqual(new_text, '前面 #H2G2 後面')

    def test_hash_2(self):
        new_text = pangu.spacing('前面#銀河便車指南 後面')
        self.assertEqual(new_text, '前面 #銀河便車指南 後面')

    def test_hash_3(self):
        new_text = pangu.spacing('前面#銀河公車指南 #銀河大客車指南 後面')
        self.assertEqual(new_text, '前面 #銀河公車指南 #銀河大客車指南 後面')

    def test_two_hash_1(self):
        new_text = pangu.spacing('前面#銀河閃電霹靂車指南#後面')
        self.assertEqual(new_text, '前面 #銀河閃電霹靂車指南# 後面')

    def test_two_hash_2(self):
        new_text = pangu.spacing('前面#H2G2#後面')
        self.assertEqual(new_text, '前面 #H2G2# 後面')

    def test_dollar(self):
        new_text = pangu.spacing('前面$後面')
        self.assertEqual(new_text, '前面 $ 後面')

    def test_percent(self):
        new_text = pangu.spacing('前面%後面')
        self.assertEqual(new_text, '前面 % 後面')

    def test_caret(self):
        new_text = pangu.spacing('前面^後面')
        self.assertEqual(new_text, '前面 ^ 後面')

    def test_ampersand(self):
        new_text = pangu.spacing('前面&後面')
        self.assertEqual(new_text, '前面 & 後面')

    def test_asterisk(self):
        new_text = pangu.spacing('前面*後面')
        self.assertEqual(new_text, '前面 * 後面')

    def test_13(self):
        new_text = pangu.spacing('前面`後面')
        self.assertEqual(new_text, '前面 ` 後面')

    def test_plus(self):
        new_text = pangu.spacing('前面+後面')
        self.assertEqual(new_text, '前面 + 後面')

    def test_minus(self):
        new_text = pangu.spacing('前面-後面')
        self.assertEqual(new_text, '前面 - 後面')

    def test_14(self):
        new_text = pangu.spacing('前面=後面')
        self.assertEqual(new_text, '前面 = 後面')

    def test_pipe(self):
        new_text = pangu.spacing('前面|後面')
        self.assertEqual(new_text, '前面 | 後面')

    def test_slash(self):
        new_text = pangu.spacing('前面/後面')
        self.assertEqual(new_text, '前面 / 後面')

    def test_backslash(self):
        new_text = pangu.spacing('前面\\後面')
        self.assertEqual(new_text, '前面 \\ 後面')

    def test_parenthese_1(self):
        new_text = pangu.spacing('前面(後面')
        self.assertEqual(new_text, '前面 ( 後面')

    def test_parenthese_2(self):
        new_text = pangu.spacing('前面)後面')
        self.assertEqual(new_text, '前面 ) 後面')

    def test_two_parentheses_1(self):
        new_text = pangu.spacing('前面(中文123漢字)後面')
        self.assertEqual(new_text, '前面 (中文 123 漢字) 後面')

    def test_two_parentheses_2(self):
        new_text = pangu.spacing('前面(中文123)後面')
        self.assertEqual(new_text, '前面 (中文 123) 後面')

    def test_two_parentheses_3(self):
        new_text = pangu.spacing('前面(123中文)後面')
        self.assertEqual(new_text, '前面 (123 中文) 後面')

    def test_two_parentheses_4(self):
        new_text = pangu.spacing('前面(中文123) then')
        self.assertEqual(new_text, '前面 (中文 123) then')

    def test_two_parentheses_5(self):
        new_text = pangu.spacing('前面(123中文) then')
        self.assertEqual(new_text, '前面 (123 中文) then')

    def test_two_parentheses_6(self):
        new_text = pangu.spacing('前面( ) then')
        self.assertEqual(new_text, '前面 ( ) then')

    def test_bracket_1(self):
        new_text = pangu.spacing('前面[後面')
        self.assertEqual(new_text, '前面 [ 後面')

    def test_bracket_2(self):
        new_text = pangu.spacing('前面]後面')
        self.assertEqual(new_text, '前面 ] 後面')

    def test_curly_bracket_1(self):
        new_text = pangu.spacing('前面{後面')
        self.assertEqual(new_text, '前面 { 後面')

    def test_curly_bracket_2(self):
        new_text = pangu.spacing('前面}後面')
        self.assertEqual(new_text, '前面 } 後面')

    def test_angle_bracket_1(self):
        new_text = pangu.spacing('前面<後面')
        self.assertEqual(new_text, '前面 < 後面')

    def test_angle_bracket_2(self):
        new_text = pangu.spacing('前面>後面')
        self.assertEqual(new_text, '前面 > 後面')

    def test_single_quote_1(self):
        new_text = pangu.spacing("前面'中文123漢字'後面")
        self.assertEqual(new_text, "前面 '中文 123 漢字' 後面")

    def test_single_quote_2(self):
        new_text = pangu.spacing("前面' '後面")
        self.assertEqual(new_text, "前面 ' ' 後面")

    def test_double_quote_1(self):
        new_text = pangu.spacing('前面"中文123漢字"後面')
        self.assertEqual(new_text, '前面 "中文 123 漢字" 後面')

    def test_double_quote_2(self):
        new_text = pangu.spacing('前面" "後面')
        self.assertEqual(new_text, '前面 " " 後面')


if __name__ == '__main__':
    unittest.main()
