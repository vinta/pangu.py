#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pangu


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()

long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read()

license = open('LICENSE').read()

requirements_lines = [line.strip() for line in open('requirements.txt').readlines()]
install_requires = list(filter(None, requirements_lines))

setup(
    name='pangu',
    version=pangu.__version__,
    description='Paranoid text spacing for good readability, to automatically insert whitespace between CJK (Chinese, Japanese, Korean) and half-width characters (alphabetical letters, numerical digits and symbols).',
    long_description=long_description,
    keywords='pangu space white text spacing readability',
    author='Vinta Chen',
    author_email='vinta.chen@gmail.com',
    url='https://github.com/vinta/pangu.py',
    license=license,
    install_requires=install_requires,
    include_package_data=True,
    py_modules=['pangu', ],
    test_suite='test_pangu',
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Japanese',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ),
)
