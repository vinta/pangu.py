#!/usr/bin/env python
# coding: utf-8
"""
Pangu Automatically insert whitespace between CJK (Chinese, Japanese, Korean) and 
    half-width characters (alphabetical letters, numerical digits and symbols).

Usage:

In Python Code:

>>> import pangu
>>> pangu.spacing('门多在github的用户名是menduo，他也有空格强迫症:)')
# output: u'门多在 github 的用户名是 menduo，他也有空格强迫症:)'

In Terminal:

# text
$ pangu "门多在github的用户名是menduo，他也有空格强迫症:)"
# output: 门多在 github 的用户名是 menduo，他也有空格强迫症:)

# file
$ pangu ~/menduo/pangu.txt
# output: 门多在 github 的用户名是 menduo，他也有空格强迫症:)。

# stdin, from file
$ pangu < ~/menduo/pangu.txt

# stdin, from pipeline
$ echo "门多在github的用户名是menduo，他也有空格强迫症:)" | pangu
$ echo "门多在github的用户名是menduo，他也有空格强迫症:)" | python -m pangu
# output: 门多在 github 的用户名是 menduo，他也有空格强迫症:)
"""

import re
import sys
import os


__version__ = '4.0.0'
__all__ = ['spacing', 'spacing_text', "spacing_file"]

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

def spacing_file(path):
    """
    spacing from file
    """
    with open(path) as f:
        fdata = f.read()
    return spacing_text(fdata)

def _is_abs_file(fpath):
    """
    check if `fpath` is a abs path and is a file.
    """
    return os.path.isabs(fpath) and os.path.isfile(fpath)

def _detect_filepath(src):
    """detect if src is a file or not, return the abs path or None.
    """
    if not src:
        return None
    
    if os.path.isabs(src) and os.path.isfile(src):
        return src
    
    if src.startswith("~"):
        abspath = os.path.expanduser(src)
        if _is_abs_file(abspath):
            return abspath
    else:
        currdir = os.path.abspath(os.path.curdir)
        abspath = os.path.join(currdir, src)
        if _is_abs_file(abspath):
            return abspath
    return None

def _space_file_or_text(src):
    """convert from file or str
    """
    if _detect_filepath(src):
        greater_text = spacing_file(src)
    else:
        greater_text = spacing_text(src)
    return greater_text

def echo(greater_text):   
    """echo to standard output
    """
    greater_text += "\n"
    greater_text = greater_text.encode("utf-8")
    if PY2:
        sys.stdout.write(greater_text)
    else:
        sys.stdout.buffer.write(greater_text)

if __name__ == "__main__":
    if not sys.stdin.isatty():
        echo(spacing_text(sys.stdin.read()))
    elif len(sys.argv) > 1:
        echo(_space_file_or_text(sys.argv[1]))
        sys.exit(0)
    else:
        print(__doc__)
        sys.exit(0)

