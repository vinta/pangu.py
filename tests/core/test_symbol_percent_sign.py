from pangu import spacing_text


def test_handle_symbol():
    assert spacing_text("前面%後面") == "前面 % 後面"
    assert spacing_text("前面 % 後面") == "前面 % 後面"
    assert spacing_text("前面100%後面") == "前面 100% 後面"

    assert spacing_text("新八的構造成分有95%是眼鏡、3%是水、2%是垃圾") == "新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾"

    assert spacing_text("丹寧控注意Levi's全館任2件25%OFF滿額再享85折！") == "丹寧控注意 Levi's 全館任 2 件 25% OFF 滿額再享 85 折！"
