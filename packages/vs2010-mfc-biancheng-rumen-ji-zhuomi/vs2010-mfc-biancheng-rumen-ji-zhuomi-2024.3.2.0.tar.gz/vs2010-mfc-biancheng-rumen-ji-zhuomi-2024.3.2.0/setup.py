#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Vs2010MfcBianchengRumenJiZhuomi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Vs2010MfcBianchengRumenJiZhuomi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="vs2010-mfc-biancheng-rumen-ji-zhuomi",
    version=Vs2010MfcBianchengRumenJiZhuomi.__version__,
    url="https://github.com/apachecn/vs2010-mfc-biancheng-rumen-ji-zhuomi",
    author=Vs2010MfcBianchengRumenJiZhuomi.__author__,
    author_email=Vs2010MfcBianchengRumenJiZhuomi.__email__,
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
    description="VS2010 MFC编程入门（鸡啄米）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "vs2010-mfc-biancheng-rumen-ji-zhuomi=Vs2010MfcBianchengRumenJiZhuomi.__main__:main",
            "Vs2010MfcBianchengRumenJiZhuomi=Vs2010MfcBianchengRumenJiZhuomi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
