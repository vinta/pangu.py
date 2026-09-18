import pytest

from pangu import space_text


def test_handle_symbol():
    assert space_text("前面:後面") == "前面: 後面"
    assert space_text("電話:123456789") == "電話: 123456789"
    assert space_text("前面:I have no idea後面") == "前面: I have no idea 後面"

    # DO NOT change if already spacing
    assert space_text("前面 : 後面") == "前面 : 後面"
    assert space_text("前面: 後面") == "前面: 後面"
    assert space_text("前面 :後面") == "前面 :後面"
    assert space_text("前面: I have no idea後面") == "前面: I have no idea 後面"


# FIXME
@pytest.mark.xfail(strict=True, reason="FIXME: it.todo upstream")
def test_handle_symbol_as_emoticon():
    assert space_text("前面:)後面") == "前面 :) 後面"


# FIXME
@pytest.mark.xfail(strict=True, reason="FIXME: it.todo upstream")
def test_handle_symbol_as_separator():
    assert space_text("前面:後面:再後面") == "前面:後面:再後面"
    assert space_text("前面:後面:再後面:更後面") == "前面:後面:再後面:更後面"
    assert space_text("前面:後面:再後面:更後面:超後面") == "前面:後面:再後面:更後面:超後面"
