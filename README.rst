pangu.py
========

.. image:: https://img.shields.io/travis/vinta/pangu.py/master.svg?style=flat-square
    :target: https://travis-ci.org/vinta/pangu.py

.. image:: https://img.shields.io/codecov/c/github/vinta/pangu.py/master.svg?style=flat-square
    :target: https://codecov.io/github/vinta/pangu.py

.. image:: https://img.shields.io/pypi/v/pangu.svg?style=flat-square
    :target: https://pypi.org/project/pangu/

.. image:: https://img.shields.io/pypi/pyversions/pangu.svg?style=flat-square
    :target: https://pypi.org/project/pangu/

.. image:: https://img.shields.io/badge/made%20with-%e2%9d%a4-ff69b4.svg?style=flat-square
    :target: https://vinta.ws/code/

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).

- `pangu.go <https://github.com/vinta/pangu>`_ (Go)
- `pangu.java <https://github.com/vinta/pangu.java>`_ (Java)
- `pangu.js <https://github.com/vinta/pangu.js>`_ (JavaScript)
- `pangu.py <https://github.com/vinta/pangu.py>`_ (Python)
- `pangu.space <https://github.com/vinta/pangu.space>`_ (Web API)

Installation
============

.. code-block:: bash

    $ pip install -U pangu

Usage
=====

In Python
---------

.. code-block:: py

    import pangu

    new_text = pangu.spacing_text('當你凝視著bug，bug也凝視著你')
    # new_text = '當你凝視著 bug，bug 也凝視著你'

    nwe_content = pangu.spacing_file('path/to/file.txt')
    # nwe_content = '與 PM 戰鬥的人，應當小心自己不要成為 PM'

In CLI
------

.. code-block:: bash

    $ pangu "請使用uname -m指令來檢查你的Linux作業系統是32位元或是[敏感词已被屏蔽]位元"
    請使用 uname -m 指令來檢查你的 Linux 作業系統是 32 位元或是 [敏感词已被屏蔽] 位元

    $ python -m pangu "為什麼小明有問題都不Google？因為他有Bing"
    為什麼小明有問題都不 Google？因為他有 Bing

    $ echo "未來的某一天，Gmail配備的AI可能會得出一個結論：想要消滅垃圾郵件最好的辦法就是消滅人類" >> path/to/file.txt
    $ pangu -f path/to/file.txt >> pangu_file.txt
    $ cat pangu_file.txt
    未來的某一天，Gmail 配備的 AI 可能會得出一個結論：想要消滅垃圾郵件最好的辦法就是消滅人類

    $ echo "心裡想的是Microservice，手裡做的是Distributed Monolith" | pangu
    心裡想的是 Microservice，手裡做的是 Distributed Monolith

    $ echo "你從什麼時候開始產生了我沒使用Monkey Patch的錯覺?" | python -m pangu
    你從什麼時候開始產生了我沒使用 Monkey Patch 的錯覺？
