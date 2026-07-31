# pangu.py

[![PyPI](https://img.shields.io/pypi/v/pangu.svg?style=flat-square)](https://pypi.org/project/pangu/)
[![Python versions](https://img.shields.io/pypi/pyversions/pangu.svg?style=flat-square)](https://pypi.org/project/pangu/)
[![Made with love](https://img.shields.io/badge/made%20with-%e2%9d%a4-ff69b4.svg?style=flat-square)](https://vinta.ws/code/)

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).

pangu.py 5.0 implements the same text-spacing algorithm as [pangu.js](https://github.com/vinta/pangu.js) v9.

- [pangu.go](https://github.com/vinta/pangu) (Go)
- [pangu.java](https://github.com/vinta/pangu.java) (Java)
- [pangu.js](https://github.com/vinta/pangu.js) (JavaScript)
- [pangu.py](https://github.com/vinta/pangu.py) (Python)
- [pangu.space](https://github.com/vinta/pangu.space) (Web API)

## Installation

```bash
$ pip install -U pangu
# or
$ uv add pangu
```

## Usage

### In Python

```python
import pangu

new_text = pangu.spacing_text("當你凝視著bug，bug也凝視著你")
# new_text = "當你凝視著 bug，bug 也凝視著你"

new_content = pangu.spacing_file("path/to/file.txt", encoding="utf-8")
# new_content = "與 PM 戰鬥的人，應當小心自己不要成為 PM"

pangu.has_proper_spacing("當你凝視著 bug，bug 也凝視著你")
# True
```

The engine is CPU-bound regex work, so there is no async API. From async code, use `await asyncio.to_thread(pangu.spacing_file, "path/to/file.txt")`.

### In CLI

```console
$ pangu "請使用uname -m指令來檢查你的Linux作業系統是32位元或是[敏感词已被屏蔽]位元"
請使用 uname -m 指令來檢查你的 Linux 作業系統是 32 位元或是 [敏感词已被屏蔽] 位元

$ pangu -t "為什麼小明有問題都不Google？因為他有Bing"
為什麼小明有問題都不 Google？因為他有 Bing

$ pangu -f path/to/file.txt
未來的某一天，Gmail 配備的 AI 可能會得出一個結論：想要消滅垃圾郵件最好的辦法就是消滅人類

$ pangu -c "心裡想的是Microservice，手裡做的是Distributed Monolith"; echo $?
Corrected: 心裡想的是 Microservice，手裡做的是 Distributed Monolith
1

$ echo "心裡想的是Microservice，手裡做的是Distributed Monolith" | pangu
心裡想的是 Microservice，手裡做的是 Distributed Monolith

$ python -m pangu "你從什麼時候開始產生了我沒使用Monkey Patch的錯覺?"
你從什麼時候開始產生了我沒使用 Monkey Patch 的錯覺?
```

- An explicit argument wins over piped stdin; stdin is read only when no argument is given.
- `-c/--check` exits 0 when the text already has proper spacing and 1 when it does not (the corrected text goes to stderr), and composes with piped stdin.
- Usage errors exit 2 (argparse convention; pangu.js exits 1).
