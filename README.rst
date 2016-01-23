pangu.py
========

.. image:: https://img.shields.io/travis/vinta/pangu.py/master.svg?style=flat-square
    :target: https://travis-ci.org/vinta/pangu.py

.. image:: https://img.shields.io/codecov/c/github/vinta/pangu.py/master.svg?style=flat-square
    :target: https://codecov.io/github/vinta/pangu.py

.. image:: https://img.shields.io/pypi/v/pangu.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pangu

.. image:: https://img.shields.io/pypi/pyversions/pangu.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pangu

.. image:: https://img.shields.io/badge/made%20with-%e2%9d%a4-ff69b4.svg?style=flat-square
    :target: https://vinta.ws

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).

- `pangu.go <https://github.com/vinta/pangu>`_ (Go)
- `pangu.java <https://github.com/vinta/pangu.java>`_ (Java)
- `pangu.js <https://github.com/vinta/pangu.js>`_ (JavaScript, both Node.js and Browser)
- `pangu.objective-c <https://github.com/Cee/pangu.objective-c>`_ (Objective-C)
- `pangu.php <https://github.com/Kunr/pangu.php>`_ (PHP)
- `pangu.py <https://github.com/vinta/pangu.py>`_ (Python)
- `pangu.rb <https://github.com/dlackty/pangu.rb>`_ (Ruby)

Installation
============

.. code-block:: bash

    $ pip install pangu

Usage
=====

.. code-block:: py

    import pangu

    pangu.spacing('新八的構造成分有95%是眼鏡、3%是水、2%是垃圾')
    # output: u'新八的構造成分有 95% 是眼鏡、3% 是水、2% 是垃圾'

    pangu.spacing_text("Mr.龍島主道：「Let's Party!各位高明博雅君子！」")
    # output: u"Mr. 龍島主道：「Let's Party! 各位高明博雅君子！」"

``spacing_text()`` is an alias of ``spacing()``.
