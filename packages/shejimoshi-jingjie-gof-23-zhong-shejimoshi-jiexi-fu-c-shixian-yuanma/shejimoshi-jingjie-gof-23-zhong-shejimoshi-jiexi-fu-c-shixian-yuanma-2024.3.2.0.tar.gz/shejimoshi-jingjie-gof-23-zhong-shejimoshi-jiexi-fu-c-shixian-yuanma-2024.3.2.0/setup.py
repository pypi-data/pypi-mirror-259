#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="shejimoshi-jingjie-gof-23-zhong-shejimoshi-jiexi-fu-c-shixian-yuanma",
    version=ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma.__version__,
    url="https://github.com/apachecn/shejimoshi-jingjie-gof-23-zhong-shejimoshi-jiexi-fu-c-shixian-yuanma",
    author=ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma.__author__,
    author_email=ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma.__email__,
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
    description="设计模式精解－GoF 23种设计模式解析附C++实现源码",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "shejimoshi-jingjie-gof-23-zhong-shejimoshi-jiexi-fu-c-shixian-yuanma=ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma.__main__:main",
            "ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma=ShejimoshiJingjieGof23ZhongShejimoshiJiexiFuCShixianYuanma.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
