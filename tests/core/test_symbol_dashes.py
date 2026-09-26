import pytest

from pangu import space_text


# \u2014
# FIXME
@pytest.mark.xfail(strict=True, reason="FIXME: it.fails upstream")
def test_handle_symbol():
    assert space_text("他說——不對") == "他說 —— 不對"
    assert space_text("台灣——美麗之島") == "台灣 —— 美麗之島"
    assert space_text("他說———不對") == "他說 ——— 不對"
    assert space_text("他說 —— 不對") == "他說 —— 不對"


# No CJK contact, no change
def test_keep_between_ans_untouched():
    assert space_text("A—B") == "A—B"
    assert space_text("2020—2024年") == "2020—2024 年"


# \u2500
# FIXME
@pytest.mark.xfail(strict=True, reason="FIXME: it.fails upstream")
def test_handle_symbol_2():
    assert space_text("他說──不對") == "他說 ── 不對"
    assert space_text("於是──各位觀眾") == "於是 ── 各位觀眾"
    assert space_text("於是 ── 各位觀眾") == "於是 ── 各位觀眾"


# No CJK contact, no change
def test_keep_between_ans_untouched_2():
    assert space_text("A─B") == "A─B"
    assert space_text("2020──2024") == "2020──2024"
