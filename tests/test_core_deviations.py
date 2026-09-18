import pytest

from pangu import _core


def test_name_suffix_max_length_covers_every_listed_name():
    parser = pytest.importorskip("re._parser")  # private CPython module, Python 3.11+
    assert parser.parse(_core.NAME_SUFFIX).getwidth()[1] <= _core.NAME_SUFFIX_MAX_LENGTH
