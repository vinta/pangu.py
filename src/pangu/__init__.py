"""Paranoid text spacing for good readability.

Automatically insert whitespace between CJK (Chinese, Japanese, Korean) and
half-width characters (alphabetical letters, numerical digits and symbols).

>>> import pangu
>>> pangu.spacing_text("當你凝視著bug，bug也凝視著你")
'當你凝視著 bug，bug 也凝視著你'
>>> pangu.spacing_file("path/to/file.txt")  # doctest: +SKIP
'與 PM 戰鬥的人，應當小心自己不要成為 PM'

The engine is CPU-bound regex work, so there is no async API; from async code use
``await asyncio.to_thread(pangu.spacing_file, path)``.
"""

from pangu._cli import cli
from pangu._core import has_proper_spacing, spacing_file, spacing_text

__version__ = "5.0.0"
__all__ = ["__version__", "cli", "has_proper_spacing", "spacing_file", "spacing_text"]
