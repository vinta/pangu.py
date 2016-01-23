# coding: utf-8

import re
import sys


__version__ = '3.0.0'
__all__ = ['spacing', 'spacing_text']

PY2 = (sys.version_info[0] == 2)

# borrow from six
if PY2:
    def u(s):
        return unicode(s.replace(r'\\', r'\\\\'), 'unicode_escape')
else:
    def u(s):
        return s

CJK_QUOTE_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(["\'])'))
QUOTE_CJK_RE = re.compile(u(r'(["\'])([\u3040-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))
FIX_QUOTE_RE = re.compile(u(r'(["\'\(\[\{<\u201c]+)(\s*)(.+?)(\s*)(["\'\)\]\}>\u201d]+)'))
FIX_SINGLE_QUOTE_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])( )(\')([A-Za-z])'))

CJK_HASH_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])(#(\S+))'))
HASH_CJK_RE = re.compile(u(r'((\S+)#)([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))

CJK_OPERATOR_ANS_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\+\-\*\/=&\\|<>])([A-Za-z0-9])'))
ANS_OPERATOR_CJK_RE = re.compile(u(r'([A-Za-z0-9])([\+\-\*\/=&\\|<>])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))

CJK_BRACKET_CJK_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\(\[\{<\u201c]+(.*?)[\)\]\}>\u201d]+)([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))
CJK_BRACKET_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([\(\[\{<\u201c>])'))
BRACKET_CJK_RE = re.compile(u(r'([\)\]\}>\u201d<])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))
FIX_BRACKET_RE = re.compile(u(r'([\(\[\{<\u201c]+)(\s*)(.+?)(\s*)([\)\]\}>\u201d]+)'))

FIX_SYMBOL_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([~!;:,\.\?\u2026])([A-Za-z0-9])'))

CJK_ANS_RE = re.compile(u(r'([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])([A-Za-z0-9`\$%\^&\*\-=\+\\\|/@\u00a1-\u00ff\u2022\u2027\u2150-\u218f])'))
ANS_CJK_RE = re.compile(u(r'([A-Za-z0-9`~\$%\^&\*\-=\+\\\|/!;:,\.\?\u00a1-\u00ff\u2022\u2026\u2027\u2150-\u218f])([\u2e80-\u2eff\u2f00-\u2fdf\u3040-\u309f\u30a0-\u30ff\u3100-\u312f\u3200-\u32ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff])'))


def spacing(text):
    """
    Perform paranoid text spacing on text. Always return unicode.
    """

    new_text = text

    # always use unicode
    if PY2 and isinstance(new_text, str):
        new_text = new_text.decode('utf-8')

    if len(new_text) < 2:
        return new_text

    new_text = CJK_QUOTE_RE.sub(r'\1 \2', new_text)
    new_text = QUOTE_CJK_RE.sub(r'\1 \2', new_text)
    new_text = FIX_QUOTE_RE.sub(r'\1\3\5', new_text)
    new_text = FIX_SINGLE_QUOTE_RE.sub(r'\1\3\4', new_text)

    new_text = CJK_HASH_RE.sub(r'\1 \2', new_text)
    new_text = HASH_CJK_RE.sub(r'\1 \3', new_text)

    new_text = CJK_OPERATOR_ANS_RE.sub(r'\1 \2 \3', new_text)
    new_text = ANS_OPERATOR_CJK_RE.sub(r'\1 \2 \3', new_text)

    old_text = new_text
    tmp_text = CJK_BRACKET_CJK_RE.sub(r'\1 \2 \4', new_text)
    new_text = tmp_text
    if old_text == tmp_text:
        new_text = CJK_BRACKET_RE.sub(r'\1 \2', new_text)
        new_text = BRACKET_CJK_RE.sub(r'\1 \2', new_text)
    new_text = FIX_BRACKET_RE.sub(r'\1\3\5', new_text)

    new_text = FIX_SYMBOL_RE.sub(r'\1\2 \3', new_text)

    new_text = CJK_ANS_RE.sub(r'\1 \2', new_text)
    new_text = ANS_CJK_RE.sub(r'\1 \2', new_text)

    return new_text

# make an alias
spacing_text = spacing


# TODO
def spacing_file(path):
    pass
