#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xuecheng-daxue-jisuanji-yu-wangluoanquan-jiangyi-cis643-644-v0-1",
    version=XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01.__version__,
    url="https://github.com/apachecn/xuecheng-daxue-jisuanji-yu-wangluoanquan-jiangyi-cis643-644-v0-1",
    author=XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01.__author__,
    author_email=XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01.__email__,
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
    description="雪城大学计算机与网络安全讲义（CIS643&644）v0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xuecheng-daxue-jisuanji-yu-wangluoanquan-jiangyi-cis643-644-v0-1=XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01.__main__:main",
            "XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01=XuechengDaxueJisuanjiYuWangluoanquanJiangyiCis643644V01.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
