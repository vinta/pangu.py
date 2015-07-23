pangu
=====

.. image:: http://img.shields.io/travis/vinta/pangu.py/master.svg?style=flat-square
    :target: https://travis-ci.org/vinta/pangu.py

.. image:: https://img.shields.io/codecov/c/github/vinta/pangu.py/master.svg?style=flat-square
    :target: https://codecov.io/github/vinta/pangu.py

.. image:: https://landscape.io/github/vinta/pangu.py/master/landscape.svg?style=flat-square
    :target: https://landscape.io/github/vinta/pangu.py/master

.. image:: http://img.shields.io/pypi/v/pangu.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pangu

.. image:: https://pypip.in/py_versions/pangu/badge.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pangu

.. image:: https://img.shields.io/badge/made%20with-%e2%9d%a4-ff69b4.svg?style=flat-square
    :target: http://vinta.ws

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).

- Go version: `pangu.go <https://github.com/vinta/pangu>`_
- Java version: `pangu.java <https://github.com/vinta/pangu.java>`_
- JavaScript version: `pangu.js <https://github.com/vinta/paranoid-auto-spacing>`_
- Node.js version: `pangu.node <https://github.com/huei90/pangu.node>`_
- Python version: `pangu.py <https://github.com/vinta/pangu.py>`_
- Ruby version: `pangu.rb <https://github.com/dlackty/pangu.rb>`_

Installation
============

.. code-block:: bash

    $ pip install pangu

Usage
=====

.. code-block:: py

    >>> import pangu

    >>> pangu.spacing(u'所以,請問Jackey的鼻子有幾個?3.14個')
    u'所以, 請問 Jackey 的鼻子有幾個? 3.14 個'

    >>> pangu.spacing(u'新八的構造成分有95%是眼鏡、3%是水、2%是垃圾')
    u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾'

    >>> pangu.spacing(u'新阿姆斯特朗炫風噴射阿姆斯特朗砲')
    u'新阿姆斯特朗炫風噴射阿姆斯特朗砲'
