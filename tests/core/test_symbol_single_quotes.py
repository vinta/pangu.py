from pangu import space_text


def test_handle_symbols_as_quotes():
    assert space_text("Why are Python's 'private' methods not actually private?") == "Why are Python's 'private' methods not actually private?"

    assert space_text("举个栗子，如果一道题只包含'A' ~ 'Z'意味着字符集大小是") == "举个栗子，如果一道题只包含 'A' ~ 'Z' 意味着字符集大小是"

    # Single quotes around Chinese text should not have spaces added
    assert space_text("Remove '铁蕾' from 1 Folder?") == "Remove '铁蕾' from 1 Folder?"


def test_handle_symbols_as_apostrophe():
    assert space_text("陳上進 likes 林依諾's status.") == "陳上進 likes 林依諾's status."
