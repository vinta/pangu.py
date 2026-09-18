from pangu import space_text


def test_handle_symbols_as_quotes():
    assert space_text("前面`中間`後面") == "前面 `中間` 後面"

    assert space_text('`! git commit -a -m "蛤"`') == '`! git commit -a -m "蛤"`'

    assert space_text("从结果来看，当a.b销毁后，`a.getB()`返回值为null") == "从结果来看，当 a.b 销毁后，`a.getB()` 返回值为 null"

    assert (
        space_text('雖然知道可以在Claude Code直接執行shell指令，例如`! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用`!`啊#TIL')
        == '雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL'
    )

    assert (
        space_text('雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL')
        == '雖然知道可以在 Claude Code 直接執行 shell 指令，例如 `! git commit -a -m "蛤"`，但是看了文件才知道原來在 http://command.md 裡面也可以用 `!` 啊 #TIL'
    )
