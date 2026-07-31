from pangu import has_proper_spacing, spacing_text


# spacingText()
def test_spacing_text():
    assert spacing_text("聽說Hadoop工程師睡不著的時候都會MapReduce羊") == "聽說 Hadoop 工程師睡不著的時候都會 MapReduce 羊"

    assert spacing_text("遇到了一個問題，決定用 thread 來解決，嗯，在現有我兩個問了題") == "遇到了一個問題，決定用 thread 來解決，嗯，在現有我兩個問了題"


def test_spacing_text_is_idempotent():
    # Formatter contract: a second pass never changes the output, so format-then-check always passes
    for text in ['"字+"', '"字|"', '你好"字+"世界', '多行"字+"\n下行"字|"', "聽說Hadoop工程師睡不著的時候都會MapReduce羊"]:
        once = spacing_text(text)
        assert spacing_text(once) == once
        assert has_proper_spacing(once) is True


# hasProperSpacing()
def test_detect_proper_spacing():
    assert has_proper_spacing("♫ 每條大街小巷，每個工程師的嘴裡，見面第一句話，就是不要在過年前 Deploy ♫") is True
    assert has_proper_spacing("♫每條大街小巷，每個工程師的嘴裡，見面第一句話，就是不要在過年前Deploy♫") is False
