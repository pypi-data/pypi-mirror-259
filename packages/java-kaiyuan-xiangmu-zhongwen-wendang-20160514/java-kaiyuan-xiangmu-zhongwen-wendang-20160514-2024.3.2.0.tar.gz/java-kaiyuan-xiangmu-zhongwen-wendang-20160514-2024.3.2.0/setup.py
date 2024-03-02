#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import JavaKaiyuanXiangmuZhongwenWendang20160514
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('JavaKaiyuanXiangmuZhongwenWendang20160514'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="java-kaiyuan-xiangmu-zhongwen-wendang-20160514",
    version=JavaKaiyuanXiangmuZhongwenWendang20160514.__version__,
    url="https://github.com/apachecn/java-kaiyuan-xiangmu-zhongwen-wendang-20160514",
    author=JavaKaiyuanXiangmuZhongwenWendang20160514.__author__,
    author_email=JavaKaiyuanXiangmuZhongwenWendang20160514.__email__,
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
    description="Java 开源项目中文文档 20160514",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "java-kaiyuan-xiangmu-zhongwen-wendang-20160514=JavaKaiyuanXiangmuZhongwenWendang20160514.__main__:main",
            "JavaKaiyuanXiangmuZhongwenWendang20160514=JavaKaiyuanXiangmuZhongwenWendang20160514.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
