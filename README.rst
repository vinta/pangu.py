pangu
=====

.. image:: https://travis-ci.org/vinta/pangu.py.png?branch=master
    :alt: Build Badge
    :target: https://travis-ci.org/vinta/pangu.py

.. image:: https://coveralls.io/repos/vinta/pangu.py/badge.png?branch=master
    :alt: Coverage Badge
    :target: https://coveralls.io/r/vinta/pangu.py

.. image:: https://badge.fury.io/py/pangu.png
    :alt: Version Badge
    :target: http://badge.fury.io/py/pangu

Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean), half-width English, digit and symbol characters.

JavaScript version: `pangu.js <https://github.com/vinta/paranoid-auto-spacing>`_
Node.js version: `pangu.node <https://github.com/huei90/pangu.node>`_
Python version: `pangu.py <https://github.com/vinta/pangu.py>`_
Java version: `pangu.java <https://github.com/vinta/pangu.java>`_

Installation
============

.. code-block:: bash

    $ pip install pangu

Usage
=====

.. code-block:: pycon

    >>> import pangu

    >>> pangu.spacing(u'請問Jackie的鼻子有幾個？123個！')
    u'請問 Jackie 的鼻子有幾個？123 個！'

    >>> pangu.spacing(u'主要成份：眼鏡95%、水3%、垃圾2%。')
    u'主要成份：眼鏡 95%、水 3%、垃圾 2%。'

    >>> pangu.spacing(u'新阿姆斯特朗炫風噴射阿姆斯特朗砲')
    u'新阿姆斯特朗炫風噴射阿姆斯特朗砲'
