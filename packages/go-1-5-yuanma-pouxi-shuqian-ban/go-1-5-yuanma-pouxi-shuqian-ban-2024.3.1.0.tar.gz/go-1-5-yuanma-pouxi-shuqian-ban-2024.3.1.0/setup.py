#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Go15YuanmaPouxiShuqianBan
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Go15YuanmaPouxiShuqianBan'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="go-1-5-yuanma-pouxi-shuqian-ban",
    version=Go15YuanmaPouxiShuqianBan.__version__,
    url="https://github.com/apachecn/go-1-5-yuanma-pouxi-shuqian-ban",
    author=Go15YuanmaPouxiShuqianBan.__author__,
    author_email=Go15YuanmaPouxiShuqianBan.__email__,
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
    description="Go 1.5 源码剖析 （书签版）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "go-1-5-yuanma-pouxi-shuqian-ban=Go15YuanmaPouxiShuqianBan.__main__:main",
            "Go15YuanmaPouxiShuqianBan=Go15YuanmaPouxiShuqianBan.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
