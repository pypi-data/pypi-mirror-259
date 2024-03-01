#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import X100GeGdbXiaoJiqiao
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('X100GeGdbXiaoJiqiao'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="x100-ge-gdb-xiao-jiqiao",
    version=X100GeGdbXiaoJiqiao.__version__,
    url="https://github.com/apachecn/x100-ge-gdb-xiao-jiqiao",
    author=X100GeGdbXiaoJiqiao.__author__,
    author_email=X100GeGdbXiaoJiqiao.__email__,
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
    description="100个gdb小技巧",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "x100-ge-gdb-xiao-jiqiao=X100GeGdbXiaoJiqiao.__main__:main",
            "X100GeGdbXiaoJiqiao=X100GeGdbXiaoJiqiao.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
