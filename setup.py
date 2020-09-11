# -*- coding: utf-8 -*-
import io
import os

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'txtop'
DESCRIPTION = 'A package for the operation of text reading and writing'
URL = 'http://github.com/dumyy/txtop'
EMAIL = 'dukuoo@foxmail.com'
AUTHOR = 'dumyy'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

here = os.path.abspath(os.path.dirname(__file__))

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      author=AUTHOR,
      author_email=EMAIL,
      python_requires=REQUIRES_PYTHON,
      url=URL,
      install_requires=[
          'numpy>=1.16.2',
          'matplotlib>=3.1.0',
      ],
      extras_require={},
      packages=find_packages(),
      include_package_data=True)
