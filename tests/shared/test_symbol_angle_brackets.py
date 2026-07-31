from pangu import spacing_text


def test_handle_symbols_as_angle_brackets():
    assert spacing_text("前面<中文123漢字>後面") == "前面 <中文 123 漢字> 後面"
    assert spacing_text("前面<中文123>後面") == "前面 <中文 123> 後面"
    assert spacing_text("前面<123漢字>後面") == "前面 <123 漢字> 後面"
    assert spacing_text("前面<中文123> tail") == "前面 <中文 123> tail"
    assert spacing_text("head <中文123漢字>後面") == "head <中文 123 漢字> 後面"
    assert spacing_text("head <中文123漢字> tail") == "head <中文 123 漢字> tail"


def test_handle_as_html_tags():
    assert spacing_text("<p>一行文本</p>") == "<p>一行文本</p>"
    assert spacing_text("<p>文字<strong>加粗</strong></p>") == "<p>文字<strong>加粗</strong></p>"
    assert spacing_text("<div>測試<span>內容</span>結束</div>") == "<div>測試<span>內容</span>結束</div>"
    assert spacing_text('<a href="#">連結</a>') == '<a href="#">連結</a>'
    assert spacing_text('<input value="測試123">') == '<input value="測試 123">'
    assert spacing_text('<img src="test.jpg" alt="測試圖片">') == '<img src="test.jpg" alt="測試圖片">'

    # Multiple tags
    assert spacing_text("<p>第一段</p><p>第二段</p>") == "<p>第一段</p><p>第二段</p>"
    assert spacing_text("<h1>標題</h1><p>內容</p>") == "<h1>標題</h1><p>內容</p>"

    # Nested tags
    assert spacing_text("<div><p>嵌套<strong>測試</strong></p></div>") == "<div><p>嵌套<strong>測試</strong></p></div>"

    # Self-closing tags
    assert spacing_text("文字<br>換行") == "文字<br>換行"
    assert spacing_text("水平線<hr>分隔") == "水平線<hr>分隔"
    assert spacing_text("水平線<hr />分隔") == "水平線<hr />分隔"

    # A bare unpaired non-void tag is a tag mention: spaced from CJK as one unit
    assert spacing_text("在這裡插入一個<div>標籤") == "在這裡插入一個 <div> 標籤"
    assert spacing_text("型別是List<String>的容器") == "型別是 List<String> 的容器"
    assert spacing_text("把文字包在<span>裡面") == "把文字包在 <span> 裡面"
    assert spacing_text("每個<li>代表一個列表項目") == "每個 <li> 代表一個列表項目"
    assert spacing_text("用<table>排版是過時的做法") == "用 <table> 排版是過時的做法"
    assert spacing_text("HTML的<head>放的是metadata") == "HTML 的 <head> 放的是 metadata"
    assert spacing_text("<html>是整份文件的根元素") == "<html> 是整份文件的根元素"

    # Generic type parameters read as tag mentions too
    assert spacing_text("回傳Promise<string>就好") == "回傳 Promise<string> 就好"
    assert spacing_text("用Vec<u8>儲存位元組") == "用 Vec<u8> 儲存位元組"
    assert spacing_text("先引入<iostream>標頭檔") == "先引入 <iostream> 標頭檔"

    # A mention next to real markup: only the mention is spaced
    assert spacing_text("<p>用<code>標記程式碼</p>") == "<p>用 <code> 標記程式碼</p>"

    # <br> or <hr> must stay untouched
    assert spacing_text("文字<br>換行") == "文字<br>換行"
    assert spacing_text("文字<br />換行") == "文字<br />換行"
    assert spacing_text("第一段<hr>第二段") == "第一段<hr>第二段"
    assert spacing_text("第一段<hr />第二段") == "第一段<hr />第二段"

    # Real-world markup stays untouched
    assert spacing_text("<ul><li>第一項</li><li>第二項</li></ul>") == "<ul><li>第一項</li><li>第二項</li></ul>"
    assert spacing_text("<button disabled>送出表單</button>") == "<button disabled>送出表單</button>"
    assert spacing_text('<img src="photo.jpg">上面是圖片') == '<img src="photo.jpg">上面是圖片'
    assert spacing_text("這裡放<Spinner />元件") == "這裡放 <Spinner /> 元件"

    # FIXME
    # assert spacing_text("<attackOnJava>那一天，人類終於回想起了，曾經一度被XML所支配的恐懼</attackOnJava> <!-- 進擊的Java -->") == "<attackOnJava>那一天，人類終於回想起了，曾經一度被 XML 所支配的恐懼</attackOnJava> <!-- 進擊的 Java -->"
