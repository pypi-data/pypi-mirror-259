#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import QingsongXuexiWeijifenYiyanGudengbao
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('QingsongXuexiWeijifenYiyanGudengbao'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="qingsong-xuexi-weijifen-yiyan-gudengbao",
    version=QingsongXuexiWeijifenYiyanGudengbao.__version__,
    url="https://github.com/apachecn/qingsong-xuexi-weijifen-yiyan-gudengbao",
    author=QingsongXuexiWeijifenYiyanGudengbao.__author__,
    author_email=QingsongXuexiWeijifenYiyanGudengbao.__email__,
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
    description="轻松学习微积分（译言古登堡）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "qingsong-xuexi-weijifen-yiyan-gudengbao=QingsongXuexiWeijifenYiyanGudengbao.__main__:main",
            "QingsongXuexiWeijifenYiyanGudengbao=QingsongXuexiWeijifenYiyanGudengbao.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
