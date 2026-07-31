from pangu import spacing_text


def test_handle_symbols_as_quotes():
    assert spacing_text("前面`中間`後面") == "前面 `中間` 後面"

    assert spacing_text('! git commit -a -m "蛤"') == '! git commit -a -m "蛤"'

    assert spacing_text('`! git commit -a -m "蛤"`') == '`! git commit -a -m "蛤"`'

    assert spacing_text("'! git commit -a -m \"蛤\"'") == "'! git commit -a -m \"蛤\"'"

    assert spacing_text("\"! git commit -a -m '蛤'\"") == "\"! git commit -a -m '蛤'\""

    assert (
        spacing_text('雖然知道可以在Claude Code直接執行shell指令，例如`! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用`!`啊#TIL')
        == '雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL'
    )

    assert (
        spacing_text('雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL')
        == '雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL'
    )
