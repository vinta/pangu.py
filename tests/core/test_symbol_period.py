from pangu import spacing_text


# Symbol . only add space on the right
def test_handle_symbol():
    assert spacing_text("前面.") == "前面."
    assert spacing_text("前面..") == "前面.."
    assert spacing_text("前面...") == "前面..."
    assert spacing_text("前面.後面") == "前面. 後面"
    assert spacing_text("前面..後面") == "前面.. 後面"
    assert spacing_text("前面...後面") == "前面... 後面"

    # DO NOT change if already spacing
    assert spacing_text("前面 . 後面") == "前面 . 後面"
    assert spacing_text("前面. 後面") == "前面. 後面"
    assert spacing_text("前面 .後面") == "前面 .後面"

    # Special cases
    assert spacing_text("前面vs.後面") == "前面 vs. 後面"
    assert spacing_text("前面U.S.A.後面") == "前面 U.S.A. 後面"
    assert spacing_text("黑人問號.jpg後面") == "黑人問號.jpg 後面"
    assert spacing_text("黑人問號.jpg 後面") == "黑人問號.jpg 後面"
    assert spacing_text("pangu.js v1.2.3橫空出世") == "pangu.js v1.2.3 橫空出世"
    assert spacing_text("pangu.js 1.2.3橫空出世") == "pangu.js 1.2.3 橫空出世"

    assert spacing_text("Mr.龍島主道：「Let's Party!各位高明博雅君子！") == "Mr. 龍島主道：「Let's Party! 各位高明博雅君子！"

    assert spacing_text("Mr.龍島主道:「Let's Party!各位高明博雅君子!") == "Mr. 龍島主道:「Let's Party! 各位高明博雅君子!"

    assert spacing_text("世.界.，草.班.与千.早.爱.音.") == "世. 界.，草. 班. 与千. 早. 爱. 音."


def test_handle_symbol_as_file_path():
    # File extensions should keep spacing
    assert spacing_text("使用Python.py檔案") == "使用 Python.py 檔案"
    assert spacing_text("設定檔.env很重要") == "設定檔.env 很重要"
    assert spacing_text("編輯器.vscode目錄") == "編輯器.vscode 目錄"

    # Multiple dots
    assert spacing_text("版本v1.2.3發布了") == "版本 v1.2.3 發布了"
    assert spacing_text("檔案package.lock.json存在") == "檔案 package.lock.json 存在"

    # CJK before dot patterns
    assert spacing_text("環境.env") == "環境.env"
    assert spacing_text("測試.test.js") == "測試.test.js"
    assert spacing_text("專案.gitignore") == "專案.gitignore"

    # Mixed patterns
    assert spacing_text("使用環境.env配置") == "使用環境.env 配置"
    assert spacing_text("專案.prettierrc和.eslintrc") == "專案.prettierrc 和.eslintrc"
