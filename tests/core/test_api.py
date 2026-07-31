from pangu import has_proper_spacing, spacing_text


# spacingText()
def test_spacing_text():
    assert spacing_text("聽說Hadoop工程師睡不著的時候都會MapReduce羊") == "聽說 Hadoop 工程師睡不著的時候都會 MapReduce 羊"

    assert spacing_text("遇到了一個問題，決定用 thread 來解決，嗯，在現有我兩個問了題") == "遇到了一個問題，決定用 thread 來解決，嗯，在現有我兩個問了題"


# hasProperSpacing()
def test_detect_proper_spacing():
    assert has_proper_spacing("♫ 每條大街小巷，每個工程師的嘴裡，見面第一句話，就是不要在過年前 Deploy ♫") is True
    assert has_proper_spacing("♫每條大街小巷，每個工程師的嘴裡，見面第一句話，就是不要在過年前Deploy♫") is False
