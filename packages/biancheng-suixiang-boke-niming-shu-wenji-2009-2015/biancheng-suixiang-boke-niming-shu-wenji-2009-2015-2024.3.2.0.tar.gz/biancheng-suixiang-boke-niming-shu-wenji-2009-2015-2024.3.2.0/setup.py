#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import BianchengSuixiangBokeNimingShuWenji20092015
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('BianchengSuixiangBokeNimingShuWenji20092015'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="biancheng-suixiang-boke-niming-shu-wenji-2009-2015",
    version=BianchengSuixiangBokeNimingShuWenji20092015.__version__,
    url="https://github.com/apachecn/biancheng-suixiang-boke-niming-shu-wenji-2009-2015",
    author=BianchengSuixiangBokeNimingShuWenji20092015.__author__,
    author_email=BianchengSuixiangBokeNimingShuWenji20092015.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="编程随想博客匿名术文集 2009~2015",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "biancheng-suixiang-boke-niming-shu-wenji-2009-2015=BianchengSuixiangBokeNimingShuWenji20092015.__main__:main",
            "BianchengSuixiangBokeNimingShuWenji20092015=BianchengSuixiangBokeNimingShuWenji20092015.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
