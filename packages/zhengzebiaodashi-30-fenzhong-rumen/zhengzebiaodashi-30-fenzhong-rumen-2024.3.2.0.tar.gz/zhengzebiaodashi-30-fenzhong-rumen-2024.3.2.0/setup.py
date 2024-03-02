#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Zhengzebiaodashi30FenzhongRumen
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Zhengzebiaodashi30FenzhongRumen'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="zhengzebiaodashi-30-fenzhong-rumen",
    version=Zhengzebiaodashi30FenzhongRumen.__version__,
    url="https://github.com/apachecn/zhengzebiaodashi-30-fenzhong-rumen",
    author=Zhengzebiaodashi30FenzhongRumen.__author__,
    author_email=Zhengzebiaodashi30FenzhongRumen.__email__,
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
    description="正则表达式30分钟入门",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "zhengzebiaodashi-30-fenzhong-rumen=Zhengzebiaodashi30FenzhongRumen.__main__:main",
            "Zhengzebiaodashi30FenzhongRumen=Zhengzebiaodashi30FenzhongRumen.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
