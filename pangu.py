# coding: utf-8

from __future__ import unicode_literals

import re


__version__ = '1.0.0'
__all__ = ['spacing', ]


CJK_QUOTE_L_RE = re.compile(r'([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(["\'])', flags=re.IGNORECASE)
CJK_QUOTE_R_RE = re.compile(r'(["\'])([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])', flags=re.IGNORECASE)
CJK_QUOTE_FIX_RE = re.compile(r'(["\']+)(\s*)(.+?)(\s*)(["\']+)', flags=re.IGNORECASE)

CJK_BRACKET_RE = re.compile(r'([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([<\[\{\(]+(.*?)[>\]\}\)]+)([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])', flags=re.IGNORECASE)
CJK_BRACKETFIX_RE = re.compile(r'([<\[\{\(]+)(\s*)(.+?)(\s*)([>\]\}\)]+)', flags=re.IGNORECASE)
CJK_BRACKET_L_RE = re.compile(r'([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([<>\[\]\{\}\(\)])', flags=re.IGNORECASE)
CJK_BRACKET_R_RE = re.compile(r'([<>\[\]\{\}\(\)])([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])', flags=re.IGNORECASE)

CJK_HASH_L_RE = re.compile(r'([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(#(\S+))', flags=re.IGNORECASE)
CJK_HASH_R_RE = re.compile(r'((\S+)#)([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])', flags=re.IGNORECASE)

CJK_L_RE = re.compile(r'([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([a-z0-9`@&%=\$\^\*\-\+\|\/\\])', flags=re.IGNORECASE)
CJK_R_RE = re.compile(r'([a-z0-9`~!%&=;\|\,\.\:\?\$\^\*\-\+\/\\])([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])', flags=re.IGNORECASE)


def spacing(text):
    text = CJK_QUOTE_L_RE.sub(r'\1 \2', text)
    text = CJK_QUOTE_R_RE.sub(r'\1 \2', text)
    text = CJK_QUOTE_FIX_RE.sub(r'\1\3\5', text)

    old_text = text
    new_text = CJK_BRACKET_RE.sub(r'\1 \2 \4', old_text)
    text = new_text
    if (old_text == new_text):
        text = CJK_BRACKET_L_RE.sub(r'\1 \2', text)
        text = CJK_BRACKET_R_RE.sub(r'\1 \2', text)
    text = CJK_BRACKETFIX_RE.sub(r'\1\3\5', text)

    text = CJK_HASH_L_RE.sub(r'\1 \2', text)
    text = CJK_HASH_R_RE.sub(r'\1 \3', text)

    text = CJK_L_RE.sub(r'\1 \2', text)
    text = CJK_R_RE.sub(r'\1 \2', text)

    return text
