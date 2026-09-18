from pangu import space_text


def test_handle_symbol_as_operator():
    assert space_text("前面-後面") == "前面 - 後面"
    assert space_text("Vinta-陳上進") == "Vinta - 陳上進"
    assert space_text("陳上進-Vinta") == "陳上進 - Vinta"

    assert (
        space_text("博客來-Rewire-神經可塑性：用神經科學突破行為模式迴圈，終結焦慮、恐慌和憂鬱，實現最佳的心理健康")
        == "博客來 - Rewire - 神經可塑性：用神經科學突破行為模式迴圈，終結焦慮、恐慌和憂鬱，實現最佳的心理健康"
    )
    assert space_text("博客來-經濟學原理 10/e Mankiw (授權經銷版)") == "博客來 - 經濟學原理 10/e Mankiw (授權經銷版)"
    assert space_text("財政部電子發票整合服務平台[自然人憑證]-歸戶設定通知") == "財政部電子發票整合服務平台 [自然人憑證] - 歸戶設定通知"
    assert space_text("博客來-4%法則：讓錢活得比你久的提領金律(電子書)") == "博客來 - 4% 法則：讓錢活得比你久的提領金律 (電子書)"
    assert space_text("长者的智慧和复杂的维斯特洛- 文章") == "长者的智慧和复杂的维斯特洛 - 文章"
    assert space_text("1976年-2018年") == "1976 年 - 2018 年"

    # DO NOT change if already spacing
    assert space_text("前面 - 後面") == "前面 - 後面"
    assert space_text("Vinta - Abc123") == "Vinta - Abc123"
    assert space_text("Vinta - 陳上進") == "Vinta - 陳上進"
    assert space_text("陳上進 - Vinta") == "陳上進 - Vinta"
    assert space_text("得到一個 A - B 的結果") == "得到一個 A - B 的結果"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta-Abc123") == "Vinta-Abc123"  # If no CJK, DO NOT change
    assert space_text("得到一個A-B的結果") == "得到一個 A-B 的結果"
    assert space_text("去5-A教室上課") == "去 5-A 教室上課"
    assert space_text("搭2-A的公車") == "搭 2-A 的公車"
    assert space_text("範圍是1-10的整數") == "範圍是 1-10 的整數"
    assert space_text("用USB-C充電") == "用 USB-C 充電"
    assert space_text("照X-RAY檢查") == "照 X-RAY 檢查"

    # Hyphenated English names
    assert (
        space_text("英文姓名須與護照上相同，包含標點符號；範例：王小明，英文名為WANG, HSIAO-MING，請於英文姓(Surname)欄位填入WANG,、英文名(Given Names)欄位填入HSIAO-MING。")
        == "英文姓名須與護照上相同，包含標點符號；範例：王小明，英文名為 WANG, HSIAO-MING，請於英文姓 (Surname) 欄位填入 WANG,、英文名 (Given Names) 欄位填入 HSIAO-MING。"
    )


def test_handle_symbol_as_preserved_pattern():
    # Compound words
    assert space_text("Sci-Fi") == "Sci-Fi"
    assert space_text("X-RAY") == "X-RAY"
    assert space_text("USB Type-C") == "USB Type-C"

    assert (
        space_text("The company offered a state-of-the-art machine-learning-powered real-time fraud-detection system with end-to-end encryption and cutting-edge performance.")
        == "The company offered a state-of-the-art machine-learning-powered real-time fraud-detection system with end-to-end encryption and cutting-edge performance."
    )

    assert (
        space_text("這間公司提供了一套state-of-the-art、machine-learning-powered的real-time fraud-detection系統，具備end-to-end加密功能以及cutting-edge的效能。")
        == "這間公司提供了一套 state-of-the-art、machine-learning-powered 的 real-time fraud-detection 系統，具備 end-to-end 加密功能以及 cutting-edge 的效能。"
    )

    assert space_text("Anthropic的claude-4-opus模型") == "Anthropic 的 claude-4-opus 模型"
    assert space_text("OpenAI的o3-pro模型") == "OpenAI 的 o3-pro 模型"
    assert space_text("OpenAI的gpt-4o模型") == "OpenAI 的 gpt-4o 模型"
    assert space_text("OpenAI的GPT-5模型") == "OpenAI 的 GPT-5 模型"
    assert space_text("Google的gemini-2.5-pro模型") == "Google 的 gemini-2.5-pro 模型"


def test_handle_symbol_as_affix():
    # CLI flags
    assert space_text("你可以使用uname -m指令來檢查你的Linux作業系統是32位元或是[敏感词已被屏蔽]位元") == "你可以使用 uname -m 指令來檢查你的 Linux 作業系統是 32 位元或是 [敏感词已被屏蔽] 位元"
    assert space_text("參數要加-m的旗標") == "參數要加 -m 的旗標"

    # Grades
    assert space_text("得到一個D-的結果") == "得到一個 D- 的結果"
    assert space_text("得到一個D--的結果") == "得到一個 D-- 的結果"

    # NOTE: fixed by AI spacing, see browser-extensions/chrome/src/ai-spacing/shapes/hyphen-digit.ts
    # The hyphen sign reading was dropped, CJK-N reads as an operator, see pangu.js ADR 0015
    # assert space_text("氣溫是-5度左右") == "氣溫是 -5 度左右"
    # assert space_text("Nasdaq-100本週下跌-13.44%") == "Nasdaq-100 本週下跌 -13.44%"
