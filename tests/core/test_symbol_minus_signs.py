from pangu import spacing_text


# When the symbol appears only 1 time or shows up with other operators in one line
def test_handle_symbol_as_operator_always_spacing():
    assert spacing_text("前面-後面") == "前面 - 後面"
    assert spacing_text("Vinta-Mollie") == "Vinta-Mollie"  # If no CJK, DO NOT change
    assert spacing_text("Vinta-陳上進") == "Vinta - 陳上進"
    assert spacing_text("陳上進-Vinta") == "陳上進 - Vinta"

    # DO NOT change if already spacing
    assert spacing_text("前面 - 後面") == "前面 - 後面"
    assert spacing_text("Vinta - Mollie") == "Vinta - Mollie"
    assert spacing_text("Vinta - 陳上進") == "Vinta - 陳上進"
    assert spacing_text("陳上進 - Vinta") == "陳上進 - Vinta"
    assert spacing_text("得到一個 A - B 的結果") == "得到一個 A - B 的結果"


def test_handle_symbol_as_hyphen_dash():
    # Compound words
    assert spacing_text("Sci-Fi") == "Sci-Fi"
    assert spacing_text("X-RAY") == "X-RAY"
    assert spacing_text("USB Type-C") == "USB Type-C"

    assert (
        spacing_text("The company offered a state-of-the-art machine-learning-powered real-time fraud-detection system with end-to-end encryption and cutting-edge performance.")
        == "The company offered a state-of-the-art machine-learning-powered real-time fraud-detection system with end-to-end encryption and cutting-edge performance."
    )

    assert (
        spacing_text("這間公司提供了一套state-of-the-art、machine-learning-powered的real-time fraud-detection系統，具備end-to-end加密功能以及cutting-edge的效能。")
        == "這間公司提供了一套 state-of-the-art、machine-learning-powered 的 real-time fraud-detection 系統，具備 end-to-end 加密功能以及 cutting-edge 的效能。"
    )

    assert spacing_text("Anthropic的claude-4-opus模型") == "Anthropic 的 claude-4-opus 模型"
    assert spacing_text("OpenAI的o3-pro模型") == "OpenAI 的 o3-pro 模型"
    assert spacing_text("OpenAI的gpt-4o模型") == "OpenAI 的 gpt-4o 模型"
    assert spacing_text("OpenAI的GPT-5模型") == "OpenAI 的 GPT-5 模型"
    assert spacing_text("Google的gemini-2.5-pro模型") == "Google 的 gemini-2.5-pro 模型"

    # Hyphen between half-width characters is a word connector, not an operator
    # Only a hyphen in direct contact with CJK acts as an operator
    assert spacing_text("得到一個A-B的結果") == "得到一個 A-B 的結果"
    assert spacing_text("去5-A教室上課") == "去 5-A 教室上課"
    assert spacing_text("搭2-A的公車") == "搭 2-A 的公車"
    assert spacing_text("範圍是1-10的整數") == "範圍是 1-10 的整數"
    assert spacing_text("用USB-C充電") == "用 USB-C 充電"
    assert spacing_text("照X-RAY檢查") == "照 X-RAY 檢查"

    # Hyphenated English names
    assert (
        spacing_text("英文姓名須與護照上相同，包含標點符號；範例：王小明，英文名為WANG,HSIAO-MING，請於英文姓(Surname)欄位填入WANG,、英文名(Given Names)欄位填入HSIAO-MING。")
        == "英文姓名須與護照上相同，包含標點符號；範例：王小明，英文名為 WANG,HSIAO-MING，請於英文姓 (Surname) 欄位填入 WANG,、英文名 (Given Names) 欄位填入 HSIAO-MING。"
    )

    # CLI flags
    assert spacing_text("你可以使用uname -m指令來檢查你的Linux作業系統是32位元或是[敏感词已被屏蔽]位元") == "你可以使用 uname -m 指令來檢查你的 Linux 作業系統是 32 位元或是 [敏感词已被屏蔽] 位元"

    assert spacing_text("得到一個D-的結果") == "得到一個 D- 的結果"
    assert spacing_text("得到一個D--的結果") == "得到一個 D-- 的結果"

    assert spacing_text("长者的智慧和复杂的维斯特洛- 文章") == "长者的智慧和复杂的维斯特洛 - 文章"

    assert spacing_text("氣溫是-5度左右") == "氣溫是 -5 度左右"
    assert spacing_text("參數要加-m的旗標") == "參數要加 -m 的旗標"

    # FIXME: a year range should read the hyphen as an operator, not as a sign attached to the second year
    # assert spacing_text("2016年-2018年") == "2016 年 - 2018 年"

    # FIXME
    # assert spacing_text("陳上進--Vinta") == "陳上進 -- Vinta"
    # assert spacing_text("陳上進---Vinta") == "陳上進 --- Vinta"
