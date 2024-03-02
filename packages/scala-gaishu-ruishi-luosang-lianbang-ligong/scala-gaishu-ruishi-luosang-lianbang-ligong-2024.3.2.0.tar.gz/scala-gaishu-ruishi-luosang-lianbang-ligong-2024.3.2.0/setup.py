#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ScalaGaishuRuishiLuosangLianbangLigong
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ScalaGaishuRuishiLuosangLianbangLigong'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="scala-gaishu-ruishi-luosang-lianbang-ligong",
    version=ScalaGaishuRuishiLuosangLianbangLigong.__version__,
    url="https://github.com/apachecn/scala-gaishu-ruishi-luosang-lianbang-ligong",
    author=ScalaGaishuRuishiLuosangLianbangLigong.__author__,
    author_email=ScalaGaishuRuishiLuosangLianbangLigong.__email__,
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
    description="Scala 概述（瑞士洛桑联邦理工）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "scala-gaishu-ruishi-luosang-lianbang-ligong=ScalaGaishuRuishiLuosangLianbangLigong.__main__:main",
            "ScalaGaishuRuishiLuosangLianbangLigong=ScalaGaishuRuishiLuosangLianbangLigong.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
