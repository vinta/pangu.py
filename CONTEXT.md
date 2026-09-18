# pangu.py

pangu.py inserts whitespace between CJK and ANS characters automatically. It ships as a text engine and a CLI. Python port of the [pangu.js](https://github.com/vinta/pangu.js) v10 text-spacing algorithm.

## Language

**Space**:
The verb for inserting whitespace: pangu spaces CJK from ANS. Spaced and unspaced are the adjectives, and tight describes a shape that stays unspaced on purpose (`A/B`). Spacing is the noun and the modifier: spacing rules, text spacing. A space is also the character itself. Public function names take the verb (`space_text()`, `space_file()`); a predicate about the concept keeps the noun (`has_proper_spacing()`).
_Avoid_: spacings (no plural)

**CJK**:
The class of Chinese, Japanese, and Korean characters. Every spacing rule depends on this class.

**ANS**:
Alphabetical letters, numerical digits, and symbols. When an ANS character is adjacent to CJK, it triggers spacing. The name lists its three parts, parallel to CJK. `A`, `N`, and `S` also name the sub-classes in code and in shapes.

**Text spacing**:
Inserting whitespace between CJK and ANS characters inside one string. For the string API it is the whole input.

## Paranoid Text Spacing Algorithm

The algorithm behind text spacing. Source of truth: `src/pangu/_core.py` (a 1:1 port of pangu.js `src/shared/index.ts`), exhaustive examples: the per-symbol files in `tests/core/` (ported from pangu.js `tests/shared/`). The shapes below are generic: `CJK` is any CJK character, `A` is any letter, `N` is any digit, and symbols are literal.

**Symbol handling**:
A symbol between two ANS characters binds them into a joiner token, and the symbol never gets spaces. A symbol in direct contact with CJK reads as an operator and gets spaces, unless an affix reading attaches it to its ANS side. `|` follows pipe reading. `+` follows plus reading. The separators `_` and `/` never get spaces.

**Joiner token**:
ANS characters that any symbol joins tight (`A/B`, `26/30`, `vinta/hal-9000`, `S&P`, `Q&A`, `A+B`, `5+5`, `foo=bar&baz=1`, `A<B`, `HSIAO-MING`). A joiner token is never split. It is spaced from adjacent CJK as one unit. Pipes and plus signs also follow pipe reading and plus reading.

**Pipe reading**:
Decided per line, never across lines. If one pipe is in direct contact with CJK, every pipe on the line becomes a separator with spaces on both sides. This covers concatenated page titles (`CJK | A CJK | A`) and credit lines (`CJK | CJK`). If no pipe on the line is in direct contact with CJK, the pipes stay tight as joiner tokens (`CJK A|A CJK`, `ps aux|grep node`).

**Plus reading**:
Decided per line, never across lines. If one plus is in direct contact with CJK, every undecided plus on the line becomes a separator with spaces on both sides. This covers bundle plans (`A CJK + A`). A plus is already decided in three cases: it is adjacent to a space, an affix reading attaches it (`N+ CJK`, `CJK +N`), or it sits inside a preserved pattern (`C++`). By default, a plus after a word is a separator (`CJK+A+CJK` reads `CJK + A + CJK`, `A+CJK` reads `A + CJK`). Listed names follow name-suffix reading. Plus reading runs before the operator rules, so a `CJK+A` contact flips the line's joiners too. If no plus on the line is in direct contact with CJK, the pluses stay tight as joiner tokens (`CJK A+A CJK`, `CJK N+N CJK`). A plus touching full-width punctuation stays tight on that side. A plus after a closing bracket is a separator before an opening full-width bracket or quote, even when it is the line's only plus. Only the closing-bracket side gets a space. See pangu.js ADR 0022.

**Affix reading**:
A symbol that attaches to its ANS side at a CJK boundary instead of reading as an operator. Four cases: `+` before digits as a sign (`CJK +N`), `-` before a lowercase flag (`CJK -m CJK`), `+` after a whole digit run as a suffix (`CJK N+ CJK`, never `AN+ CJK`), and single-letter grades (`A+`, `D-`). A plus after a word is not an affix: `A+CJK` reads as a separator (`A + CJK`); see plus reading and pangu.js ADR 0019. A hyphen before digits is not an affix: `CJK-N` reads as an operator (`N CJK - N CJK`, `CJK - N CJK`); see pangu.js ADR 0015. A capitalized word after a hyphen keeps the operator reading (`CJK - Vinta`).

**Superscript suffix**:
A Unicode superscript character, or a mark that renders raised (`™`, `℠`, `®`), that attaches to whatever is on its left, CJK or ANS, and is spaced from CJK on its right (`CJK² CJK`, `A² CJK`). It is not an affix reading, since it attaches to either side. `⁽` is not a suffix, so the space never lands inside a superscript parenthesis (`CJK⁽CJK⁾ CJK`). See pangu.js ADR 0021.

**Name suffix**:
A `+` or `-` attached to a listed name, such as `Disney+`, `公視+`, or `AB-`. It stays tight where the author wrote it tight. See pangu.js ADR 0024.

**No CJK contact, no change**:
The invariant behind every symbol rule. ANS text that has no contact with CJK is never modified. A symbol must be in direct contact with CJK to read as an operator. So CJK elsewhere in the line or text never allows spacing between ANS characters.

**Pattern preservation**:
Some tokens keep their internal shape, even where an operator reading would otherwise apply: compound words (`state-of-the-art`, `GPT-5`, `claude-4-opus`), programming terms (`C++`, `A+`, `i++`, `D-`, `C#`, `F#`), arrow tokens (`=>`, `->`), glob patterns (`*.log`, `templates/*.html`), and file paths (`/usr/bin`, `src/main.py`, `C:\Users\`).

**Punctuation**:
Half-width punctuation is not converted to full-width, with two exceptions. A colon that is in direct contact with CJK and sits right before a parenthesis becomes the full-width colon `\uFF1A`. Middle dots (`\u00B7` `\u2022` `\u2027`) normalize to the katakana middle dot `\u30FB`. Multiple consecutive punctuation marks are preserved. One or more of `!` `;` `,` `?` whose right side is in direct contact with CJK always get a trailing space, no matter what is on their left (`(N CJK),CJK`, `N%,CJK`). So a stray space that is typed before the mark is rewritten, not preserved.

**HTML**:
Tags are protected from spacing rules. Text inside attributes is processed. The exception is a tag mention, which is spaced.

**Tag mention**:
A bare tag with no attributes, a non-void name, and no closing counterpart anywhere in the text. It can be self-closing or not (`CJK <div> CJK`, `CJK List<String> CJK`, `CJK <Spinner /> CJK`). A tag mention reads as one unit that is mentioned in prose, not as markup: it is spaced where it is in direct contact with CJK, and tight against ANS characters. Paired tags, void elements (`<br>`, `<br />`), and tags with attributes stay protected markup.

**HTTP URL**:
An address that starts with `http://` or `https://`. It reads as one unit: nothing inside it is modified, and it is spaced from CJK on its left. It ends at whitespace, quotes, brackets, or CJK punctuation; CJK characters belong to it, so CJK prose written tight after it stays tight. Trailing half-width punctuation and an unbalanced closing parenthesis belong to the prose. A URL inside an attribute value is the same unit. See pangu.js ADR 0026.

## Porting

Upstream is pangu.js v10. `src/pangu/_core.py` deliberately stays js-shaped — same UPPER_SNAKE pattern names, same load-bearing pipeline order — so each upstream release ports as a mechanical diff; do not "clean it up" (see `docs/adr/0001-traceable-core-pythonic-surface.md`). The public surface (module functions, argparse CLI, packaging) is idiomatic Python and deviates deliberately. The 1:1 test suite in `tests/core/` (mirroring pangu.js `tests/shared/`) is the parity spec.

## Agent Skill Overrides

**handoff**: write handoff documents to `./tmp/handoff-<topic>.md` (repo root) instead of the OS temp directory, so they survive a reboot. `/tmp/` is already gitignored via `~/.gitignore_global`; no further ignore rule needed.
