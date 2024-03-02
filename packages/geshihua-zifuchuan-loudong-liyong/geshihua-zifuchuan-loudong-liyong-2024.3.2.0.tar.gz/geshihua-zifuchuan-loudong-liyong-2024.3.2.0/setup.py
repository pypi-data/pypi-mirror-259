#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import GeshihuaZifuchuanLoudongLiyong
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('GeshihuaZifuchuanLoudongLiyong'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="geshihua-zifuchuan-loudong-liyong",
    version=GeshihuaZifuchuanLoudongLiyong.__version__,
    url="https://github.com/apachecn/geshihua-zifuchuan-loudong-liyong",
    author=GeshihuaZifuchuanLoudongLiyong.__author__,
    author_email=GeshihuaZifuchuanLoudongLiyong.__email__,
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
    description="格式化字符串漏洞利用",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "geshihua-zifuchuan-loudong-liyong=GeshihuaZifuchuanLoudongLiyong.__main__:main",
            "GeshihuaZifuchuanLoudongLiyong=GeshihuaZifuchuanLoudongLiyong.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
