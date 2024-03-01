#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import X100GeGccXiaoJiqiao
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('X100GeGccXiaoJiqiao'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="x100-ge-gcc-xiao-jiqiao",
    version=X100GeGccXiaoJiqiao.__version__,
    url="https://github.com/apachecn/x100-ge-gcc-xiao-jiqiao",
    author=X100GeGccXiaoJiqiao.__author__,
    author_email=X100GeGccXiaoJiqiao.__email__,
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
    description="100个gcc小技巧",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "x100-ge-gcc-xiao-jiqiao=X100GeGccXiaoJiqiao.__main__:main",
            "X100GeGccXiaoJiqiao=X100GeGccXiaoJiqiao.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
