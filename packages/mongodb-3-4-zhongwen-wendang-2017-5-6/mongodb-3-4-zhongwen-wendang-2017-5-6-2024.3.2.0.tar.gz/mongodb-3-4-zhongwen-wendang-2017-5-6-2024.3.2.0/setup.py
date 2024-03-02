#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Mongodb34ZhongwenWendang201756
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Mongodb34ZhongwenWendang201756'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mongodb-3-4-zhongwen-wendang-2017-5-6",
    version=Mongodb34ZhongwenWendang201756.__version__,
    url="https://github.com/apachecn/mongodb-3-4-zhongwen-wendang-2017-5-6",
    author=Mongodb34ZhongwenWendang201756.__author__,
    author_email=Mongodb34ZhongwenWendang201756.__email__,
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
    description="MongoDB 3.4 中文文档 2017.5.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mongodb-3-4-zhongwen-wendang-2017-5-6=Mongodb34ZhongwenWendang201756.__main__:main",
            "Mongodb34ZhongwenWendang201756=Mongodb34ZhongwenWendang201756.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
