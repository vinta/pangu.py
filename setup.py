#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read()

license = open('LICENSE').read()

requirements_lines = [line.strip() for line in open('requirements.txt').readlines()]
install_requires = list(filter(None, requirements_lines))

setup(
    name='pangu',
    version='1.0.0',
    description='Spacing texts using Python! Insert a white space between full-width characters (Chinese, Japanese, etc.) and half-width alphanumerics. For good readability.',
    long_description=long_description,
    keywords='white space text spacing readability',
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
        'Development Status :: 3 - Alpha',
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
        'Programming Language :: Python :: 3',
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
