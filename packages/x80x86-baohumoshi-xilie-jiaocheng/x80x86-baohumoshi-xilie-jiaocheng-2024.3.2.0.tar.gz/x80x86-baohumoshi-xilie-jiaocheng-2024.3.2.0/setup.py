#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import X80x86BaohumoshiXilieJiaocheng
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('X80x86BaohumoshiXilieJiaocheng'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="x80x86-baohumoshi-xilie-jiaocheng",
    version=X80x86BaohumoshiXilieJiaocheng.__version__,
    url="https://github.com/apachecn/x80x86-baohumoshi-xilie-jiaocheng",
    author=X80x86BaohumoshiXilieJiaocheng.__author__,
    author_email=X80x86BaohumoshiXilieJiaocheng.__email__,
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
    description="80x86保护模式系列教程",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "x80x86-baohumoshi-xilie-jiaocheng=X80x86BaohumoshiXilieJiaocheng.__main__:main",
            "X80x86BaohumoshiXilieJiaocheng=X80x86BaohumoshiXilieJiaocheng.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
