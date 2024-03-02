#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="sitanfu-jiqi-xuexi-geren-biji-v4-2-huanghai-guang",
    version=SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang.__version__,
    url="https://github.com/apachecn/sitanfu-jiqi-xuexi-geren-biji-v4-2-huanghai-guang",
    author=SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang.__author__,
    author_email=SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang.__email__,
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
    description="斯坦福机器学习个人笔记 v4.2 - 黄海广",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "sitanfu-jiqi-xuexi-geren-biji-v4-2-huanghai-guang=SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang.__main__:main",
            "SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang=SitanfuJiqiXuexiGerenBijiV42HuanghaiGuang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
