#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import TheSwiftProgrammingLanguageZhongwenbanV12
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('TheSwiftProgrammingLanguageZhongwenbanV12'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="the-swift-programming-language-zhongwenban-v1-2",
    version=TheSwiftProgrammingLanguageZhongwenbanV12.__version__,
    url="https://github.com/apachecn/the-swift-programming-language-zhongwenban-v1-2",
    author=TheSwiftProgrammingLanguageZhongwenbanV12.__author__,
    author_email=TheSwiftProgrammingLanguageZhongwenbanV12.__email__,
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
    description="The Swift Programming Language 中文版 - v1.2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "the-swift-programming-language-zhongwenban-v1-2=TheSwiftProgrammingLanguageZhongwenbanV12.__main__:main",
            "TheSwiftProgrammingLanguageZhongwenbanV12=TheSwiftProgrammingLanguageZhongwenbanV12.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
