#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ApacheZeppelin072ZhongwenWendang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ApacheZeppelin072ZhongwenWendang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="apache-zeppelin-0-7-2-zhongwen-wendang",
    version=ApacheZeppelin072ZhongwenWendang.__version__,
    url="https://github.com/apachecn/apache-zeppelin-0-7-2-zhongwen-wendang",
    author=ApacheZeppelin072ZhongwenWendang.__author__,
    author_email=ApacheZeppelin072ZhongwenWendang.__email__,
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
    description="Apache Zeppelin 0.7.2 中文文档",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "apache-zeppelin-0-7-2-zhongwen-wendang=ApacheZeppelin072ZhongwenWendang.__main__:main",
            "ApacheZeppelin072ZhongwenWendang=ApacheZeppelin072ZhongwenWendang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
