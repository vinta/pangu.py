pangu
=====

.. image:: http://img.shields.io/travis/vinta/pangu.py.svg
    :alt: Build Badge
    :target: https://travis-ci.org/vinta/pangu.py

.. image:: http://img.shields.io/coveralls/vinta/pangu.py.svg
    :alt: Coverage Badge
    :target: https://coveralls.io/r/vinta/pangu.py

.. image:: http://img.shields.io/pypi/v/pangu.svg
    :alt: Version Badge
    :target: http://badge.fury.io/py/pangu

.. image:: https://d2weczhvl823v0.cloudfront.net/vinta/pangu.py/trend.png
    :alt: Bitdeli badge
    :target: https://bitdeli.com/free

Spacing texts using Python! Insert a white space between full-width characters (Chinese, Japanese, etc.) and half-width alphanumerics. For good readability.

JavaScript version: `pangu.js <https://github.com/vinta/paranoid-auto-spacing>`_

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
