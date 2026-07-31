# pangu.py

[![PyPI Version](https://img.shields.io/pypi/v/pangu.svg?style=for-the-badge)](https://pypi.org/project/pangu/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pangu.svg?style=for-the-badge)](https://pypi.org/project/pangu/)

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).

- [pangu.js](https://github.com/vinta/pangu.js)
- [pangu.py](https://github.com/vinta/pangu.py)
- [pangu.go](https://github.com/vinta/pangu)
- [pangu.java](https://github.com/vinta/pangu.java)
- [pangu.space](https://github.com/vinta/pangu.space)

## Installation

```bash
$ uv add pangu
# or
$ pip install -U pangu
```

## Usage

### In Python

```python
import pangu

new_text = pangu.spacing_text("你從什麼時候開始產生了我沒使用Monkey Patch的錯覺?")
# new_text = "你從什麼時候開始產生了我沒使用 Monkey Patch 的錯覺?"

new_content = pangu.spacing_file("path/to/file.txt", encoding="utf-8")
# new_content = "與 PM 戰鬥的人，應當小心自己不要成為 PM"

pangu.has_proper_spacing("聽說 Hadoop 工程師睡不著的時候都會 Map/Reduce 羊")
# True
```

### In CLI

```bash
$ pangu-py "請使用uname -m指令來檢查你的Linux作業系統是32位元或是[敏感词已被屏蔽]位元"
請使用 uname -m 指令來檢查你的 Linux 作業系統是 32 位元或是 [敏感词已被屏蔽] 位元

$ pangu-py -t "為什麼小明有問題都不Google？因為他有Bing"
為什麼小明有問題都不 Google？因為他有 Bing

$ pangu-py -f path/to/file.txt
未來的某一天，Gmail 配備的 AI 可能會得出一個結論：想要消滅垃圾郵件最好的辦法就是消滅人類

$ pangu-py -c "心裡想的是Microservice，手裡做的是Distributed Monolith"; echo $?
Corrected: 心裡想的是 Microservice，手裡做的是 Distributed Monolith
1

$ echo "Workaround雖可恥但有用" | pangu-py
Workaround 雖可恥但有用

$ python -m pangu "聽說桐島rm -rf /*了"
聽說桐島 rm -rf /* 了
```

## License

Released under the [MIT License](https://opensource.org/licenses/MIT).

## Author

- GitHub: [@vinta](https://github.com/vinta)
- Twitter: [@vinta](https://twitter.com/vinta)
- Website: [vinta.ws](https://vinta.ws/code/)
