from pangu import space_text


def test_handle_symbol_as_separator():
    assert space_text("前面/後面") == "前面/後面"
    assert space_text("Vinta/貓咪") == "Vinta/貓咪"
    assert space_text("貓咪/Vinta") == "貓咪/Vinta"
    assert space_text("速度是60公里/小時") == "速度是 60 公里/小時"
    assert space_text("價格是$100/每小時") == "價格是 $100/每小時"
    assert space_text("我/你\n他/她") == "我/你\n他/她"
    assert space_text("歡迎光臨/再見\n參考 https://example.com/docs") == "歡迎光臨/再見\n參考 https://example.com/docs"

    # DO NOT change if already spacing
    assert space_text("前面 / 後面") == "前面 / 後面"
    assert space_text("Vinta / Abc123") == "Vinta / Abc123"
    assert space_text("Abc123 / 陳上進") == "Abc123 / 陳上進"
    assert space_text("陳上進 / Abc123") == "陳上進 / Abc123"
    assert space_text("得到一個 A / B 的結果") == "得到一個 A / B 的結果"
    assert space_text("好人 / bad guy") == "好人 / bad guy"
    assert space_text("吃apple / banana") == "吃 apple / banana"


def test_handle_symbol_as_joiner_token():
    assert space_text("Vinta/Abc123") == "Vinta/Abc123"  # If no CJK, DO NOT change
    assert space_text("得到一個A/B的結果") == "得到一個 A/B 的結果"
    assert space_text("他要做A/B測試") == "他要做 A/B 測試"
    assert space_text("打東東26/30") == "打東東 26/30"
    assert space_text("打東東1/denominator") == "打東東 1/denominator"
    assert space_text("吃apple/banana") == "吃 apple/banana"
    assert space_text("選A/B其中一個") == "選 A/B 其中一個"
    assert space_text("答案是6/2的商數") == "答案是 6/2 的商數"
    assert space_text("安装指令：npx skills add vinta/hal-9000") == "安装指令：npx skills add vinta/hal-9000"


def test_handle_symbol_as_list():
    assert space_text("陳上進/貓咪/Abc123") == "陳上進/貓咪/Abc123"
    assert space_text("陳上進/Abc123/貓咪") == "陳上進/Abc123/貓咪"
    assert space_text("Abc123/Vinta/貓咪") == "Abc123/Vinta/貓咪"
    assert space_text("Abc123/陳上進/貓咪") == "Abc123/陳上進/貓咪"
    assert space_text("日期是2024/01/22的早上") == "日期是 2024/01/22 的早上"

    assert (
        space_text("8964/3★集會所接待員/克隆·麻煩大師/手卷師傅（已退休）/主程式毀滅者/dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/NS編號在banner裡/discord:史單力#3230")
        == "8964/3★集會所接待員/克隆・麻煩大師/手卷師傅（已退休）/主程式毀滅者/dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/NS 編號在 banner 裡/discord: 史單力 #3230"
    )

    assert (
        space_text("8964/3★集會所接待員/克隆·麻煩大師/手卷師傅(已退休)/主程式毀滅者/dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/NS編號在banner裡/discord:史單力#3230")
        == "8964/3★集會所接待員/克隆・麻煩大師/手卷師傅 (已退休)/主程式毀滅者/dae-dae-o/#絕地家庭小會議/#今天大掃除了沒有/NS 編號在 banner 裡/discord: 史單力 #3230"
    )

    assert (
        space_text("after 80'/气象工作者/不苟同/关注abc天气变化/向往123自由/热爱科学、互联网、编程Node.js Web C++ Julia Python")
        == "after 80'/气象工作者/不苟同/关注 abc 天气变化/向往 123 自由/热爱科学、互联网、编程 Node.js Web C++ Julia Python"
    )

    # DO NOT change if already spacing
    assert space_text("陳上進 / 貓咪 / Abc123") == "陳上進 / 貓咪 / Abc123"
    assert space_text("陳上進 / Abc123 / 貓咪") == "陳上進 / Abc123 / 貓咪"
    assert space_text("Abc123 / Vinta / 貓咪") == "Abc123 / Vinta / 貓咪"
    assert space_text("Abc123 / 陳上進 / 貓咪") == "Abc123 / 陳上進 / 貓咪"

    assert space_text("2016-12-26(奇幻电影节) / 2017-01-20(美国) / 詹姆斯麦卡沃伊") == "2016-12-26 (奇幻电影节) / 2017-01-20 (美国) / 詹姆斯麦卡沃伊"


def test_handle_symbol_as_unix_absolute_file_path():
    assert space_text("/home和/root是Linux中的頂級目錄") == "/home 和 /root 是 Linux 中的頂級目錄"

    assert space_text("/home/與/root是Linux中的頂級目錄") == "/home/ 與 /root 是 Linux 中的頂級目錄"

    assert space_text('"/home/"和"/root"是Linux中的頂級目錄') == '"/home/" 和 "/root" 是 Linux 中的頂級目錄'

    assert space_text("當你用cat和od指令查看/dev/random和/dev/urandom的內容時") == "當你用 cat 和 od 指令查看 /dev/random 和 /dev/urandom 的內容時"

    assert space_text('當你用cat和od指令查看"/dev/random"和"/dev/urandom"的內容時') == '當你用 cat 和 od 指令查看 "/dev/random" 和 "/dev/urandom" 的內容時'

    # Basic Unix paths
    assert space_text("在/home目錄") == "在 /home 目錄"
    assert space_text("查看/etc/passwd文件") == "查看 /etc/passwd 文件"
    assert space_text("進入/usr/local/bin目錄") == "進入 /usr/local/bin 目錄"

    # Paths with dots
    assert space_text("配置檔在/etc/nginx/nginx.conf") == "配置檔在 /etc/nginx/nginx.conf"
    assert space_text("隱藏檔案/.bashrc很重要") == "隱藏檔案 /.bashrc 很重要"
    assert space_text("查看/home/.config/settings") == "查看 /home/.config/settings"

    # Paths with version numbers
    assert space_text("安裝到/usr/lib/python3.9/") == "安裝到 /usr/lib/python3.9/"
    assert space_text("位於/opt/node-v16.14.0/bin") == "位於 /opt/node-v16.14.0/bin"

    # Paths with special characters
    assert space_text("備份到/mnt/backup.2024-01-01/") == "備份到 /mnt/backup.2024-01-01/"
    assert space_text("日誌在/var/log/app-name.log") == "日誌在 /var/log/app-name.log"

    # Paths with @ symbols (npm packages)
    assert space_text("模組在/node_modules/@babel/core") == "模組在 /node_modules/@babel/core"
    assert space_text("套件在/node_modules/@types/node") == "套件在 /node_modules/@types/node"

    # Paths with + symbols
    assert space_text("編譯器在/usr/bin/g++") == "編譯器在 /usr/bin/g++"

    assert space_text("套件在/usr/lib/gcc/x86_64-linux-gnu/11++") == "套件在 /usr/lib/gcc/x86_64-linux-gnu/11++"

    # Paths ending with slash before CJK
    assert space_text("目錄/usr/bin/包含執行檔") == "目錄 /usr/bin/ 包含執行檔"
    assert space_text("資料夾/etc/nginx/存放設定") == "資料夾 /etc/nginx/ 存放設定"


def test_handle_symbol_as_unix_relative_file_path():
    # Basic relative paths
    assert space_text("檢查src/main.py文件") == "檢查 src/main.py 文件"
    assert space_text("構建dist/index.js完成") == "構建 dist/index.js 完成"
    assert space_text("運行test/spec.js測試") == "運行 test/spec.js 測試"
    assert space_text("編輯docs/README.md文檔") == "編輯 docs/README.md 文檔"

    # Project directories
    assert space_text("查看templates/base.html模板") == "查看 templates/base.html 模板"
    assert space_text("複製assets/images/logo.png圖片") == "複製 assets/images/logo.png 圖片"
    assert space_text("配置config/database.yml設定") == "配置 config/database.yml 設定"
    assert space_text("執行scripts/deploy.sh腳本") == "執行 scripts/deploy.sh 腳本"

    # Build/output directories
    assert space_text("清理build/temp/目錄") == "清理 build/temp/ 目錄"
    assert space_text("輸出到target/release/資料夾") == "輸出到 target/release/ 資料夾"
    assert space_text("發布到public/static/路徑") == "發布到 public/static/ 路徑"

    # Development directories
    assert space_text("安裝node_modules/@babel/core套件") == "安裝 node_modules/@babel/core 套件"
    assert space_text("設定.git/hooks/pre-commit鉤子") == "設定 .git/hooks/pre-commit 鉤子"
    assert space_text("編輯.vscode/settings.json配置") == "編輯 .vscode/settings.json 配置"

    # With leading ./
    assert space_text("參考./docs/API.md文件") == "參考 ./docs/API.md 文件"
    assert space_text("執行./scripts/test.sh腳本") == "執行 ./scripts/test.sh 腳本"
    assert space_text("查看./.claude/CLAUDE.md說明") == "查看 ./.claude/CLAUDE.md 說明"

    # Nested paths
    assert space_text("位於src/components/Button/index.tsx") == "位於 src/components/Button/index.tsx"
    assert space_text("存放在assets/fonts/Inter/Regular.woff2") == "存放在 assets/fonts/Inter/Regular.woff2"

    # Multiple file paths in one sentence
    assert space_text("從src/utils.js複製到dist/utils.js") == "從 src/utils.js 複製到 dist/utils.js"
    assert space_text("比較test/fixtures/input.txt和test/fixtures/output.txt") == "比較 test/fixtures/input.txt 和 test/fixtures/output.txt"


def test_handle_symbol_as_glob_pattern():
    assert space_text("聽說桐島rm -rf /*了") == "聽說桐島 rm -rf /* 了"
    assert space_text("模板在templates/*.html裡") == "模板在 templates/*.html 裡"
    assert space_text("測試所有test/**/*.js檔案") == "測試所有 test/**/*.js 檔案"
