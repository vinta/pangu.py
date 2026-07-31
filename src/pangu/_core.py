"""1:1 port of the Paranoid Text Spacing engine from pangu.js v9.

Mapping: this module ports `pangu.js/src/shared/index.ts` — same UPPER_SNAKE pattern
names, same load-bearing pipeline order — so each upstream release ports as a
mechanical diff (see docs/adr/0001). `Pangu.spacingText()` becomes `spacing_text()`,
`Pangu.hasProperSpacing()` becomes `has_proper_spacing()`, and `spacingFileSync()`
from `pangu.js/src/node/index.ts` becomes `spacing_file()`.

Deviations forced by Python's `re`:

- js `\\b` and `\\w` are ASCII while Python's are Unicode (CJK counts as `\\w`), so
  patterns relying on them compile with `re.ASCII`
- stdlib `re` rejects variable-length lookbehind, so AN_LEFT_BRACKET and
  ANS_CJK_RIGHT_QUOTE_ANY_RIGHT_QUOTE check their left context in code instead

Known, accepted delta: the few remaining `\\s` uses (PIPE_SEPARATOR, PLUS_SEPARATOR,
BARE_HTML_TAG, HTML_TAG_PATTERN) keep js/py whitespace semantics differences —
js counts U+FEFF as whitespace, Python counts U+001C-U+001F — which no ported test
observes; explicit classes are used only where behavior demanded it (CJK_HASH).
"""

import os
import re
from pathlib import Path
from typing import ClassVar

# CJK is short for Chinese, Japanese, and Korean
#
# ANS is short for Alphabets, Numbers, and Symbols:
# A includes A-Za-z plus Greek and Coptic
# N includes 0-9
# S varies per rule, see the symbol sets below
#
# For more about Unicode blocks, see https://symbl.cc/en/unicode-table/

# Unicode blocks. A name that ends in a carve-out marks a range that is deliberately smaller than its whole block, so widening it back to the block boundary is a wrong edit, not a tidy-up
CJK_RADICALS_SUPPLEMENT = r"\u2e80-\u2eff"
KANGXI_RADICALS = r"\u2f00-\u2fdf"
HIRAGANA = r"\u3040-\u309f"
KATAKANA_NO_MIDDLE_DOT = r"\u30a0-\u30fa\u30fc-\u30ff"  # The Katakana block ends at \u30ff, but \u30fb is the character that MIDDLE_DOT normalizes to, so it must not read as CJK itself
BOPOMOFO = r"\u3100-\u312f"
ENCLOSED_CJK_LETTERS_AND_MONTHS = r"\u3200-\u32ff"
CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A = r"\u3400-\u4dbf"
CJK_UNIFIED_IDEOGRAPHS = r"\u4e00-\u9fff"
CJK_COMPATIBILITY_IDEOGRAPHS = r"\uf900-\ufaff"
GREEK_AND_COPTIC = r"\u0370-\u03ff"
# The Latin-1 Supplement block starts at \u0080, but this range starts one past NBSP (\u00a0) so an NBSP lands in no character class at all. See pangu.js ADR 0009
LATIN_1_SUPPLEMENT_AFTER_NBSP = r"\u00a1-\u00ff"
NUMBER_FORMS = r"\u2150-\u218f"
DINGBATS = r"\u2700-\u27bf"

CJK = (
    f"{CJK_RADICALS_SUPPLEMENT}{KANGXI_RADICALS}{HIRAGANA}{KATAKANA_NO_MIDDLE_DOT}{BOPOMOFO}{ENCLOSED_CJK_LETTERS_AND_MONTHS}"
    f"{CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A}{CJK_UNIFIED_IDEOGRAPHS}{CJK_COMPATIBILITY_IDEOGRAPHS}"
)

# Basic character classes
AN = "A-Za-z0-9"
A = "A-Za-z"
UPPER_AN = "A-Z0-9"  # For FIX_CJK_COLON_ANS

# Operators. Each rule uses a different set
OPERATORS_BASE = r"\+\*=&"
OPERATORS_WITH_HYPHEN = rf"{OPERATORS_BASE}\-"  # For CJK_OPERATOR_ANS
OPERATORS_NO_PLUS = r"\*=&\-"  # For ANS_OPERATOR_CJK only. No + because + attaches to the preceding half-width run as a suffix (Disney+, 18+)
GRADE_OPERATORS = r"\+\-\*"  # For single letter grades

QUOTES = '`"\u05f4'  # Backtick, straight quote, Hebrew punctuation

# Brackets. Each rule uses a different set
LEFT_BRACKETS_BASIC = r"\(\[\{"  # For AN_LEFT_BRACKET
RIGHT_BRACKETS_BASIC = r"\)\]\}"  # For RIGHT_BRACKET_AN
LEFT_BRACKETS_EXTENDED = r"\(\[\{<>\u201c"  # For CJK_LEFT_BRACKET (includes angle brackets + curly quote)
RIGHT_BRACKETS_EXTENDED = r"\)\]\}<>\u201d"  # For RIGHT_BRACKET_CJK

# ANS extended sets. The two sets are not identical, see the inline notes
# Both ranges start at \u00a1, one past NBSP (\u00a0), so an NBSP is in no character class at all. That inertness is load-bearing: an NBSP already separates the runs it sits between,
# so no rule matches across it and none fires. pangu therefore never rewrites an author's NBSP, it only inserts a space where one is genuinely missing. See pangu.js ADR 0009
ANS_CJK_AFTER = rf"{A}{GREEK_AND_COPTIC}0-9@\$%\^&\*\-\+\\={LATIN_1_SUPPLEMENT_AFTER_NBSP}{NUMBER_FORMS}{DINGBATS}"  # Has @, no punctuation
ANS_BEFORE_CJK = rf"{A}{GREEK_AND_COPTIC}0-9\$%\^&\*\-\+\\={LATIN_1_SUPPLEMENT_AFTER_NBSP}{NUMBER_FORMS}{DINGBATS}"  # No @ symbol

# Common directory names in Unix and project paths
FILE_PATH_DIRS = (
    r"home|root|usr|etc|var|opt|tmp|dev|mnt|proc|sys|bin|boot|lib|media|run|sbin|srv|node_modules"
    r"|path|project|src|dist|test|tests|docs|templates|assets|public|static|config|scripts|tools|build|out|target|your|\.claude|\.git|\.vscode"
)
FILE_PATH_CHARS = r"[A-Za-z0-9_\-\.@\+\*]+"

# Unix absolute paths: system directories and common project paths, for example /home, /usr/bin, /etc/nginx.conf, /.bashrc, /node_modules/@babel/core, /path/to/your/project
UNIX_ABSOLUTE_FILE_PATH = rf"/(?:\.?(?:{FILE_PATH_DIRS})|\.(?:[A-Za-z0-9_\-]+))(?:/{FILE_PATH_CHARS})*"

# Unix relative paths that are common in documentation and blog posts, for example src/main.py, dist/index.js, test/spec.js, ./.claude/CLAUDE.md, templates/*.html
UNIX_RELATIVE_FILE_PATH = rf"(?:\./)?(?:{FILE_PATH_DIRS})(?:/{FILE_PATH_CHARS})+"

# Windows paths: C:\Users\name\, D:\Program Files\, C:\Windows\System32
WINDOWS_FILE_PATH = r"[A-Z]:\\(?:[A-Za-z0-9_\-\. ]+\\?)+"

ANY_CJK = re.compile(rf"[{CJK}]")

# A punctuation run after CJK gets a trailing space and never converts to full-width. Space only when CJK, a letter, or a digit follows, so nothing changes at the end of the text
CJK_PUNCTUATION = re.compile(rf"([{CJK}])([!;,\?:]+)(?=[{CJK}{AN}])")
# A punctuation run directly before CJK gets a space after it, whatever sits on its left (no left anchor). An already-typed 'CJK ,CJK' shape is a typo, not preserved. See pangu.js ADR 0007
# CJK_PUNCTUATION still owns colon and punctuation before letters and digits
PUNCTUATION_CJK = re.compile(rf"([!;,\?]+)(?=[{CJK}])")
# Tilde has its own rule so ~= stays intact. Space only when CJK, a letter, or a digit follows
CJK_TILDE = re.compile(rf"([{CJK}])(~+)(?!=)(?=[{CJK}{AN}])")
CJK_TILDE_EQUALS = re.compile(rf"([{CJK}])(~=)")
# Period has its own rule so file extensions, dot runs, and file paths stay intact; DOTS_CJK handles runs of dots first. Space only when CJK, a letter, or a digit follows
CJK_PERIOD = re.compile(rf"([{CJK}])(\.)(?![{AN}\./])(?=[{CJK}{AN}])")
AN_PERIOD_CJK = re.compile(rf"([{AN}])(\.)([{CJK}])")
AN_COLON_CJK = re.compile(rf"([{AN}])(:)([{CJK}])")
DOTS_CJK = re.compile(rf"([\.]{{2,}}|\u2026)([{CJK}])")
# The only case where a colon converts to full-width: after CJK, before an uppercase letter, a digit, or a parenthesis
FIX_CJK_COLON_ANS = re.compile(rf"([{CJK}])\:([{UPPER_AN}\(\)])")

# The quote class deliberately excludes ' because single quotes have their own rules
CJK_QUOTE = re.compile(rf"([{CJK}])([{QUOTES}])")
QUOTE_CJK = re.compile(rf"([{QUOTES}])([{CJK}])")
# The content class is [\s\S] rather than . so a quoted segment that spans a line break still pairs with its own closing quote. HTML source wrapping puts newlines mid-sentence, and with . that
# closing quote is unreachable, so the scan resyncs on the next quote, pairs closing-to-opening and strips the spaces outside the quotes instead of inside
FIX_QUOTE_ANY_QUOTE = re.compile(rf"([{QUOTES}]+)[ ]*([\s\S]+?)[ ]*([{QUOTES}]+)")

# Curly quotes only: CJK_QUOTE, QUOTE_CJK, and FIX_QUOTE_ANY_QUOTE already handle straight quotes
QUOTE_AN = re.compile(rf"([\u201d])([{AN}])")

# A straight quote between CJK and AN (CJK"AN) reads as closing a quoted CJK phrase, so the space goes after the quote
CJK_QUOTE_AN = re.compile(rf'([{CJK}])(")([{AN}])')

CJK_SINGLE_QUOTE_BUT_POSSESSIVE = re.compile(rf"([{CJK}])('[^s])")
SINGLE_QUOTE_CJK = re.compile(rf"(')([{CJK}])")
FIX_POSSESSIVE_SINGLE_QUOTE = re.compile(rf"([{AN}{CJK}])( )('s)")
# Single quotes whose content is only CJK characters
SINGLE_QUOTE_PURE_CJK = re.compile(rf"(')([{CJK}]+)(')")

HASH_ANS_CJK_HASH = re.compile(rf"([{CJK}])(#)([{CJK}]+)(#)([{CJK}])")
# The negated class is the "something is glued to this #, so it is a hashtag" guard, so it has to reject an NBSP the same way it rejects a space. It stays a literal pair rather than \S because \S
# also excludes zero-width characters like U+FEFF, and treating those as a gap would drop the space entirely and leave the runs flush
CJK_HASH = re.compile(rf"([{CJK}])(#([^ \u00a0]))")
HASH_CJK = re.compile(rf"(([^ \u00a0])#)([{CJK}])")
# In file path context (multiple slashes), only a final hashtag not preceded by a slash gets a space
CJK_FINAL_HASHTAG = re.compile(rf"([^/])([{CJK}])(#[A-Za-z0-9]+)$")

# The operator set is + - * = & only (no | / < >). Only direct CJK contact makes a symbol an operator: a symbol between two half-width characters binds them into a joiner token (A+B, a=1, S&P)
# and never gets spaces, so there is deliberately no between-half-width rule here
CJK_OPERATOR_ANS = re.compile(rf"([{CJK}])([{OPERATORS_WITH_HYPHEN}])([{AN}])")
ANS_OPERATOR_CJK = re.compile(rf"([{AN}])([{OPERATORS_NO_PLUS}])([{CJK}])")

# Slash patterns for operator vs separator behavior
CJK_SLASH_CJK = re.compile(rf"([{CJK}])([/])([{CJK}])")
CJK_SLASH_ANS = re.compile(rf"([{CJK}])([/])([{AN}])")
ANS_SLASH_CJK = re.compile(rf"([{AN}])([/])([{CJK}])")

# Pipe patterns for separator vs joiner-token behavior, decided per line
PIPE_CJK_CONTACT = re.compile(rf"[{CJK}]\||\|[{CJK}]")
PIPE_SEPARATOR = re.compile(r"([^\s|])[ ]*(\|+)[ ]*(?=[^\s|])")

# Plus patterns for separator vs joiner-token behavior, decided per line like the pipe. The separator matches a solitary plus only: a space-adjacent plus is settled and a ++ run is a preserved
# pattern (C++, i++)
PLUS_CJK_CONTACT = re.compile(rf"[{CJK}]\+|\+[{CJK}]")
PLUS_SEPARATOR = re.compile(r"(?<=[^\s+])\+(?=[^\s+])")

# Single-letter grades (A+, B-, C*) before CJK get the space after the symbol, not before. The \b keeps the letter single, not the tail of a longer word
# (re.ASCII: js \b is ASCII-word-based; Python's default \b counts CJK as word characters)
SINGLE_LETTER_GRADE_CJK = re.compile(rf"\b([{A}])([{GRADE_OPERATORS}])([{CJK}])", re.ASCII)

# Affix readings attach a symbol to its half-width side at a CJK boundary, overriding the operator reading
# Sign: + or - attaches to following digits (+886, -5)
CJK_SIGN_DIGIT = re.compile(rf"([{CJK}])([\+\-])([0-9])")
# Flag: - attaches to a following single lowercase letter (-m). [a-z] keeps a capitalized word on the operator reading, and the trailing \b keeps a longer lowercase word there too
CJK_HYPHEN_FLAG = re.compile(rf"([{CJK}])(\-)([a-z])\b", re.ASCII)
# Suffix: + attaches to a preceding half-width run (Disney+, 18+)
AN_PLUS_CJK = re.compile(rf"([{AN}])(\+)([{CJK}])")

# < and > as comparison operators, not brackets
CJK_LESS_THAN = re.compile(rf"([{CJK}])(<)([{AN}])")
LESS_THAN_CJK = re.compile(rf"([{AN}])(<)([{CJK}])")
CJK_GREATER_THAN = re.compile(rf"([{CJK}])(>)([{AN}])")
GREATER_THAN_CJK = re.compile(rf"([{AN}])(>)([{CJK}])")

# Bracket patterns: ( ) [ ] { } plus < >, which also act as comparison operators
# The curly quotes \u201c and \u201d appear in CJK_LEFT_BRACKET/RIGHT_BRACKET_CJK, but the paired-quote patterns handle them primarily
CJK_LEFT_BRACKET = re.compile(rf"([{CJK}])([{LEFT_BRACKETS_EXTENDED}])")
RIGHT_BRACKET_CJK = re.compile(rf"([{RIGHT_BRACKETS_EXTENDED}])([{CJK}])")
ANS_CJK_LEFT_BRACKET_ANY_RIGHT_BRACKET = re.compile(rf"([{AN}{CJK}])[ ]*([\u201c])([{AN}{CJK}\-_ ]+)([\u201d])")
LEFT_BRACKET_ANY_RIGHT_BRACKET_ANS_CJK = re.compile(rf"([\u201c])([{AN}{CJK}\-_ ]+)([\u201d])[ ]*([{AN}{CJK}])")
# Some input habits type both quotes of a pair as closing curly quotes (\u201d): the shape CJK\u201dCJK\u201d appears where CJK\u201cCJK\u201d was meant
# A \u201d only opens a \u201d...\u201d pair when no unclosed \u201c precedes it on the line (the lookbehind), otherwise it closes that \u201c
# Runs after RIGHT_BRACKET_CJK, so the [ ]* after the opener strips the space that rule just added inside the pair
# js expresses "no unclosed \u201c precedes it" as the variable-length lookbehind (?<![\u201c][^\u201c\u201d\n]*), which stdlib re rejects;
# _sub_ans_cjk_right_quote_any_right_quote() applies this pattern and checks that left context in code
ANS_CJK_RIGHT_QUOTE_ANY_RIGHT_QUOTE = re.compile(rf"([{AN}{CJK}])[ ]*([\u201d])[ ]*([{AN}{CJK}\-_ ]+?)[ ]*([\u201d])")

# A dotted name keeps its call parenthesis tight (`Math.floor(x)`, `array.map(fn)`), a bare name does not (`foo (x)`)
# js guards this with the variable-length lookbehind (?<!\.[A-Za-z0-9]*), which stdlib re rejects; _sub_an_left_bracket() applies this pattern and checks that left context in code
AN_LEFT_BRACKET = re.compile(rf"([{AN}])([{LEFT_BRACKETS_BASIC}])")
RIGHT_BRACKET_AN = re.compile(rf"([{RIGHT_BRACKETS_BASIC}])([{AN}])")

CJK_UNIX_ABSOLUTE_FILE_PATH = re.compile(rf"([{CJK}])({UNIX_ABSOLUTE_FILE_PATH})")
CJK_UNIX_RELATIVE_FILE_PATH = re.compile(rf"([{CJK}])({UNIX_RELATIVE_FILE_PATH})")
CJK_WINDOWS_PATH = re.compile(rf"([{CJK}])({WINDOWS_FILE_PATH})")

UNIX_ABSOLUTE_FILE_PATH_SLASH_CJK = re.compile(rf"({UNIX_ABSOLUTE_FILE_PATH}/)([{CJK}])")
UNIX_RELATIVE_FILE_PATH_SLASH_CJK = re.compile(rf"({UNIX_RELATIVE_FILE_PATH}/)([{CJK}])")

CJK_ANS = re.compile(rf"([{CJK}])([{ANS_CJK_AFTER}])")
ANS_CJK = re.compile(rf"([{ANS_BEFORE_CJK}])([{CJK}])")

S_A = re.compile(rf"(%)([{A}])")

MIDDLE_DOT = re.compile(r"([ ]*)([\u00b7\u2022\u2027])([ ]*)")

# A bare unpaired non-void tag amid prose is a tag mention, not markup: it reads as one unit and is spaced from CJK it directly touches
# A trailing self-closing slash is still bare, but void elements render on their own (<br> or <hr>), so they stay markup even unpaired
VOID_HTML_TAGS = frozenset({"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"})
BARE_HTML_TAG = re.compile(r"^<([a-zA-Z][a-zA-Z0-9]*)\s*/?>$")
CLOSING_HTML_TAG = re.compile(r"</([a-zA-Z][a-zA-Z0-9]*)")

# Matches only opening, closing, and self-closing tags with a real tag name, so stray < > content is not read as a tag
HTML_TAG_PATTERN = re.compile(r"</?[a-zA-Z][a-zA-Z0-9]*(?:\s+[^>]*)?>")
# Attribute values inside a tag (re.ASCII: js \w is ASCII)
HTML_TAG_ATTRIBUTE = re.compile(r'(\w+)="([^"]*)"', re.ASCII)

# Spacing at direct CJK contact with a tag mention placeholder (\uE002...\uE003)
CJK_HTML_TAG_MENTION = re.compile(rf"([{CJK}])(?=\ue002)")
HTML_TAG_MENTION_CJK = re.compile(rf"(?<=\ue003)([{CJK}])")

BACKTICK_CONTENT = re.compile(r"`([^`]+)`")

# Hyphen-joined alphanumeric runs that read as one name, for example state-of-the-art, GPT-4o, claude-4-opus. At least one part must contain a lowercase letter or mix letters with digits (GPT-5)
COMPOUND_WORD_PATTERN = re.compile(
    r"\b(?:[A-Za-z0-9]*[a-z][A-Za-z0-9]*-[A-Za-z0-9]+|[A-Za-z0-9]+-[A-Za-z0-9]*[a-z][A-Za-z0-9]*|[A-Za-z]+-[0-9]+|[A-Za-z]+[0-9]+-[A-Za-z0-9]+)(?:-[A-Za-z0-9]+)*\b",
    re.ASCII,
)

# Used by _fix_bracket_spacing() to strip the spaces just inside a bracket pair; everything else between the brackets stays unchanged
BRACKET_PATTERNS = [
    (re.compile(r"<([^<>]*)>"), "<", ">"),
    (re.compile(r"\(([^()]*)\)"), "(", ")"),
    (re.compile(r"\[([^\[\]]*)\]"), "[", "]"),
    (re.compile(r"\{([^{}]*)\}"), "{", "}"),
]
# \Z, not $: Python's $ also matches before a trailing newline (js's $ does not), which would delete a mid-content space in multiline bracket content
BRACKET_INNER_SPACES = re.compile(r"^ +| +\Z")

_AN_CHARS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")


class PlaceholderReplacer:
    """Stores text snippets and swaps them for opaque indexed placeholders until restore."""

    # Every spacing_text() call creates instances from the same few fixed configs, so compiled patterns are cached and shared across instances
    _pattern_cache: ClassVar[dict[str, re.Pattern[str]]] = {}

    def __init__(self, placeholder: str, start_delimiter: str, end_delimiter: str) -> None:
        self.items: list[str] = []
        self.index = 0
        self.placeholder = placeholder
        self.start_delimiter = start_delimiter
        self.end_delimiter = end_delimiter
        cache_key = f"{start_delimiter}{placeholder}{end_delimiter}"
        pattern = PlaceholderReplacer._pattern_cache.get(cache_key)
        if pattern is None:
            # [0-9] rather than \d: js \d is ASCII-only, Python's matches all Unicode digits
            pattern = re.compile(f"{re.escape(start_delimiter)}{placeholder}([0-9]+){re.escape(end_delimiter)}")
            PlaceholderReplacer._pattern_cache[cache_key] = pattern
        self.pattern = pattern

    def store(self, item: str) -> str:
        self.items.append(item)
        stored = f"{self.start_delimiter}{self.placeholder}{self.index}{self.end_delimiter}"
        self.index += 1
        return stored

    def restore(self, text: str) -> str:
        if self.index == 0:
            return text

        def replace(match: re.Match[str]) -> str:
            index = int(match.group(1))
            return self.items[index] if index < len(self.items) else ""

        return self.pattern.sub(replace, text)


def _has_unclosed_left_quote_before(text: str, pos: int) -> bool:
    """Port of the js lookbehind (?<![\u201c][^\u201c\u201d\\n]*) at ``pos``: is the nearest “ ” or newline to the left an unclosed “?"""
    for i in range(pos - 1, -1, -1):
        char = text[i]
        if char == "\u201c":
            return True
        if char in {"\u201d", "\n"}:
            return False
    return False


def _sub_ans_cjk_right_quote_any_right_quote(text: str) -> str:
    """Apply ANS_CJK_RIGHT_QUOTE_ANY_RIGHT_QUOTE with its lookbehind guard checked in code.

    Mirrors js matching exactly: when the guard fails, the scan resumes one character
    past the failed match's start (not past its end), so overlapping candidates are
    still found.
    """
    result: list[str] = []
    pos = 0
    while True:
        match = ANS_CJK_RIGHT_QUOTE_ANY_RIGHT_QUOTE.search(text, pos)
        if match is None:
            break
        if _has_unclosed_left_quote_before(text, match.start(2)):
            result.append(text[pos : match.start() + 1])
            pos = match.start() + 1
            continue
        result.append(text[pos : match.start()])
        result.append(f"{match.group(1)} {match.group(2)}{match.group(3)}{match.group(4)}")
        pos = match.end()
    result.append(text[pos:])
    return "".join(result)


def _sub_an_left_bracket(text: str) -> str:
    """Apply AN_LEFT_BRACKET with its lookbehind guard checked in code.

    A failed match (alphanumeric + bracket) cannot overlap a later match, so a plain
    sub() that returns the match unchanged is equivalent to js's resume-at-start+1.
    """

    def replace(match: re.Match[str]) -> str:
        # js lookbehind (?<!\.[A-Za-z0-9]*): walk left over the alphanumeric run; a dot right before it means a file extension
        i = match.start(2) - 1
        while i >= 0 and text[i] in _AN_CHARS:
            i -= 1
        if i >= 0 and text[i] == ".":
            return match.group(0)
        return f"{match.group(1)} {match.group(2)}"

    return AN_LEFT_BRACKET.sub(replace, text)


def _spacing_hashtags_in_line(line: str) -> str:
    # Slash reading is per line, so each line's slash count decides its own hashtag behavior
    if line.count("/") <= 1:
        line = CJK_HASH.sub(r"\1 \2", line)
        return HASH_CJK.sub(r"\1 \3", line)
    # Multiple slashes read as a path: no hashtag spacing except a final hashtag not preceded by a slash
    return CJK_FINAL_HASHTAG.sub(r"\1\2 \3", line, count=1)


def _spacing_slashes_in_line(line: str) -> str:
    # Slash reading is per line: the line's only slash acts as an operator when CJK touches it. Repeated slashes read as a file path or a list and get no spaces
    # A slash between half-width characters binds tight as a slash token, so no rule fires on it; file paths need no extra protection because the path rules already spaced their CJK edges
    if line.count("/") != 1:
        return line
    line = CJK_SLASH_CJK.sub(r"\1 \2 \3", line)
    line = CJK_SLASH_ANS.sub(r"\1 \2 \3", line)
    return ANS_SLASH_CJK.sub(r"\1 \2 \3", line)


def _spacing_pipes_in_line(line: str) -> str:
    # Pipe reading is per line: a pipe in direct CJK contact makes every pipe on the line a separator with spaces on both sides (CJK | CJK, as in concatenated page titles)
    # A line whose pipes touch no CJK keeps them tight as joiner tokens (x|y, ps aux|grep node)
    if not PIPE_CJK_CONTACT.search(line):
        return line
    return PIPE_SEPARATOR.sub(r"\1 \2 ", line)


def _spacing_pluses_in_line(line: str) -> str:
    # Plus reading is per line: a plus in direct contact with CJK makes every unsettled plus on the line a separator with spaces on both sides, as in telecom bundle plans that chain products with +
    # A settled plus keeps its reading: space-adjacent, affix-attached (Disney+, +886), or in a ++ run (C++). A line with no CJK contact keeps its joiner tokens tight (A+B, 5+5)
    if not PLUS_CJK_CONTACT.search(line):
        return line
    return PLUS_SEPARATOR.sub(" + ", line)


def _fix_bracket_spacing(text: str) -> str:
    # Strip the spaces that earlier rules left just inside a bracket pair: no space after an opening bracket or before a closing bracket
    for pattern, open_bracket, close_bracket in BRACKET_PATTERNS:

        def replace(match: re.Match[str], open_bracket: str = open_bracket, close_bracket: str = close_bracket) -> str:
            inner_content = match.group(1)
            if not inner_content:
                return f"{open_bracket}{close_bracket}"
            trimmed_content = BRACKET_INNER_SPACES.sub("", inner_content)
            return f"{open_bracket}{trimmed_content}{close_bracket}"

        text = pattern.sub(replace, text)
    return text


def spacing_text(text: str) -> str:  # noqa: PLR0915 too-many-statements — the js pipeline runs as one ordered sequence and the order is load-bearing (ADR 0001)
    """Insert whitespace between CJK and half-width characters in ``text``."""
    if len(text) <= 1 or not ANY_CJK.search(text):
        return text

    new_text = text

    # Hide backtick content from the quote rules; the backticks themselves still get spacing
    backtick_manager = PlaceholderReplacer("BACKTICK_CONTENT_", "\ue004", "\ue005")
    new_text = BACKTICK_CONTENT.sub(lambda match: f"`{backtick_manager.store(match.group(1))}`", new_text)

    html_tag_manager = PlaceholderReplacer("HTML_TAG_PLACEHOLDER_", "\ue000", "\ue001")
    mentioned_tag_manager = PlaceholderReplacer("HTML_TAG_MENTION_", "\ue002", "\ue003")
    has_html_tags = False

    if "<" in new_text:
        has_html_tags = True

        # Tag names whose closing tag appears anywhere in the text: their opening tags are paired markup
        closed_tag_names = {closing_tag.group(1).lower() for closing_tag in CLOSING_HTML_TAG.finditer(new_text)}

        def replace_html_tag(match: re.Match[str]) -> str:
            tag = match.group(0)
            bare_tag = BARE_HTML_TAG.match(tag)
            if bare_tag:
                tag_name = bare_tag.group(1).lower()
                if tag_name not in VOID_HTML_TAGS and tag_name not in closed_tag_names:
                    return mentioned_tag_manager.store(tag)
            # Process attribute values inside the tag
            processed_tag = HTML_TAG_ATTRIBUTE.sub(lambda attr_match: f'{attr_match.group(1)}="{spacing_text(attr_match.group(2))}"', tag)
            return html_tag_manager.store(processed_tag)

        # Hide every real tag behind a placeholder; attribute values get spacing first
        new_text = HTML_TAG_PATTERN.sub(replace_html_tag, new_text)

    # Dot runs go first, before the single-period rule
    new_text = DOTS_CJK.sub(r"\1 \2", new_text)

    new_text = CJK_PUNCTUATION.sub(r"\1\2 ", new_text)
    new_text = PUNCTUATION_CJK.sub(r"\1 ", new_text)
    new_text = CJK_TILDE.sub(r"\1\2 ", new_text)
    new_text = CJK_TILDE_EQUALS.sub(r"\1 \2 ", new_text)
    new_text = CJK_PERIOD.sub(r"\1\2 ", new_text)
    new_text = AN_PERIOD_CJK.sub(r"\1\2 \3", new_text)
    new_text = AN_COLON_CJK.sub(r"\1\2 \3", new_text)
    new_text = FIX_CJK_COLON_ANS.sub(r"\1：\2", new_text)

    new_text = CJK_QUOTE.sub(r"\1 \2", new_text)
    new_text = QUOTE_CJK.sub(r"\1 \2", new_text)
    new_text = FIX_QUOTE_ANY_QUOTE.sub(r"\1\2\3", new_text)

    new_text = QUOTE_AN.sub(r"\1 \2", new_text)
    new_text = CJK_QUOTE_AN.sub(r"\1\2 \3", new_text)

    new_text = FIX_POSSESSIVE_SINGLE_QUOTE.sub(r"\1's", new_text)

    # Quoted pure-CJK content keeps its quotes tight, so hide it before the single-quote rules run
    single_quote_cjk_manager = PlaceholderReplacer("SINGLE_QUOTE_CJK_PLACEHOLDER_", "\ue030", "\ue031")

    new_text = SINGLE_QUOTE_PURE_CJK.sub(lambda match: single_quote_cjk_manager.store(match.group(0)), new_text)

    new_text = CJK_SINGLE_QUOTE_BUT_POSSESSIVE.sub(r"\1 \2", new_text)
    new_text = SINGLE_QUOTE_CJK.sub(r"\1 \2", new_text)

    new_text = single_quote_cjk_manager.restore(new_text)

    # HASH_ANS_CJK_HASH pattern needs at least 5 characters
    if len(new_text) >= 5:  # noqa: PLR2004 magic-value-comparison — the 5 is the pattern's own minimum width, as in js
        new_text = HASH_ANS_CJK_HASH.sub(r"\1 \2\3\4 \5", new_text)
    # Slash reading is per line, so each line's slash count decides its own hashtag behavior
    new_text = "\n".join(_spacing_hashtags_in_line(line) for line in new_text.split("\n"))

    # Protect compound words from operator spacing
    compound_word_manager = PlaceholderReplacer("COMPOUND_WORD_PLACEHOLDER_", "\ue010", "\ue011")

    new_text = COMPOUND_WORD_PATTERN.sub(lambda match: compound_word_manager.store(match.group(0)), new_text)

    # Single-letter grades run before the general operator rules so A+CJK becomes A+ CJK, not A + CJK
    new_text = SINGLE_LETTER_GRADE_CJK.sub(r"\1\2 \3", new_text)

    # Affix readings run before the operator rules so the symbol stays attached to its half-width side
    new_text = CJK_SIGN_DIGIT.sub(r"\1 \2\3", new_text)
    new_text = CJK_HYPHEN_FLAG.sub(r"\1 \2\3", new_text)
    new_text = AN_PLUS_CJK.sub(r"\1\2 \3", new_text)

    new_text = CJK_OPERATOR_ANS.sub(r"\1 \2 \3", new_text)
    new_text = ANS_OPERATOR_CJK.sub(r"\1 \2 \3", new_text)

    new_text = CJK_LESS_THAN.sub(r"\1 \2 \3", new_text)
    new_text = LESS_THAN_CJK.sub(r"\1 \2 \3", new_text)
    new_text = CJK_GREATER_THAN.sub(r"\1 \2 \3", new_text)
    new_text = GREATER_THAN_CJK.sub(r"\1 \2 \3", new_text)

    new_text = CJK_UNIX_ABSOLUTE_FILE_PATH.sub(r"\1 \2", new_text)
    new_text = CJK_UNIX_RELATIVE_FILE_PATH.sub(r"\1 \2", new_text)
    new_text = CJK_WINDOWS_PATH.sub(r"\1 \2", new_text)

    new_text = UNIX_ABSOLUTE_FILE_PATH_SLASH_CJK.sub(r"\1 \2", new_text)
    new_text = UNIX_RELATIVE_FILE_PATH_SLASH_CJK.sub(r"\1 \2", new_text)

    new_text = "\n".join(_spacing_slashes_in_line(line) for line in new_text.split("\n"))
    new_text = "\n".join(_spacing_pipes_in_line(line) for line in new_text.split("\n"))
    new_text = "\n".join(_spacing_pluses_in_line(line) for line in new_text.split("\n"))

    new_text = compound_word_manager.restore(new_text)

    new_text = CJK_LEFT_BRACKET.sub(r"\1 \2", new_text)
    new_text = RIGHT_BRACKET_CJK.sub(r"\1 \2", new_text)
    new_text = ANS_CJK_LEFT_BRACKET_ANY_RIGHT_BRACKET.sub(r"\1 \2\3\4", new_text)
    new_text = LEFT_BRACKET_ANY_RIGHT_BRACKET_ANS_CJK.sub(r"\1\2\3 \4", new_text)
    new_text = _sub_ans_cjk_right_quote_any_right_quote(new_text)

    new_text = _sub_an_left_bracket(new_text)
    new_text = RIGHT_BRACKET_AN.sub(r"\1 \2", new_text)

    new_text = CJK_ANS.sub(r"\1 \2", new_text)
    new_text = ANS_CJK.sub(r"\1 \2", new_text)

    new_text = S_A.sub(r"\1 \2", new_text)

    new_text = MIDDLE_DOT.sub("・", new_text)

    new_text = _fix_bracket_spacing(new_text)

    # Restore HTML tags from placeholders (only if HTML processing occurred)
    if has_html_tags:
        # A tag mention reads as one unit: space it from CJK it directly touches
        new_text = CJK_HTML_TAG_MENTION.sub(r"\1 ", new_text)
        new_text = HTML_TAG_MENTION_CJK.sub(r" \1", new_text)
        new_text = mentioned_tag_manager.restore(new_text)
        new_text = html_tag_manager.restore(new_text)

    return backtick_manager.restore(new_text)


def has_proper_spacing(text: str) -> bool:
    """Return whether ``text`` already has proper spacing."""
    return spacing_text(text) == text


def spacing_file(path: str | os.PathLike[str], *, encoding: str = "utf-8") -> str:
    """Read the file at ``path`` and return its content with spacing applied."""
    # Decode bytes directly, not read_text(): text mode's universal newlines would rewrite \r\n and \r to \n, while js readFileSync preserves line endings
    return spacing_text(Path(path).read_bytes().decode(encoding))
