# coding: utf-8

from __future__ import unicode_literals
import re
import sys


_py_version = sys.version_info
is_py2 = (_py_version[0] == 2)

__version__ = '2.5.6.2'
__all__ = ['spacing', ]


CJK_QUOTE_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(["\'])')
QUOTE_CJK_RE = re.compile(r'(["\'])([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')
FIX_QUOTE_RE = re.compile(r'(["\'\(\[\{<\u201c]+)(\s*)(.+?)(\s*)(["\'\)\]\}>\u201d]+)')
FIX_SINGLE_QUOTE_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])( )(\')([A-Za-z])')

CJK_HASH_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(#(\S+))')
HASH_CJK_RE = re.compile(r'((\S+)#)([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')

CJK_OPERATOR_ANS_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\+\-\*\/=&\\|<>])([A-Za-z0-9])')
ANS_OPERATOR_CJK_RE = re.compile(r'([A-Za-z0-9])([\+\-\*\/=&\\|<>])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')

CJK_BRACKET_CJK_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\(\[\{<\u201c]+(.*?)[\)\]\}>\u201d]+)([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')
CJK_BRACKET_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\(\[\{<\u201c>])')
BRACKET_CJK_RE = re.compile(r'([\)\]\}>\u201d<])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')
FIX_BRACKET_RE = re.compile(r'([\(\[\{<\u201c]+)(\s*)(.+?)(\s*)([\)\]\}>\u201d]+)')

FIX_SYMBOL_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([~!;:,\.\?\u2026])([A-Za-z0-9])')

CJK_ANS_RE = re.compile(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([A-Za-z0-9`\$%\^&\*\-=\+\\\|/@\u00a1-\u00ff\u2022\u2027\u2150-\u218f])')
ANS_CJK_RE = re.compile(r'([A-Za-z0-9`~\$%\^&\*\-=\+\\\|/!;:,\.\?\u00a1-\u00ff\u2022\u2026\u2027\u2150-\u218f])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])')


def spacing(text):
    """
    Perform paranoid text spacing on text. Always return Unicode.
    """

    if is_py2 and isinstance(text, str):
        text = text.decode('utf-8')

    if len(text) < 2:
        return text

    text = CJK_QUOTE_RE.sub(r'\1 \2', text)
    text = QUOTE_CJK_RE.sub(r'\1 \2', text)
    text = FIX_QUOTE_RE.sub(r'\1\3\5', text)
    text = FIX_SINGLE_QUOTE_RE.sub(r'\1\3\4', text)

    text = CJK_HASH_RE.sub(r'\1 \2', text)
    text = HASH_CJK_RE.sub(r'\1 \3', text)

    text = CJK_OPERATOR_ANS_RE.sub(r'\1 \2 \3', text)
    text = ANS_OPERATOR_CJK_RE.sub(r'\1 \2 \3', text)

    old_text = text
    new_text = CJK_BRACKET_CJK_RE.sub(r'\1 \2 \4', old_text)
    text = new_text
    if old_text == new_text:
        text = CJK_BRACKET_RE.sub(r'\1 \2', text)
        text = BRACKET_CJK_RE.sub(r'\1 \2', text)
    text = FIX_BRACKET_RE.sub(r'\1\3\5', text)

    text = FIX_SYMBOL_RE.sub(r'\1\2 \3', text)

    text = CJK_ANS_RE.sub(r'\1 \2', text)
    text = ANS_CJK_RE.sub(r'\1 \2', text)

    return text
