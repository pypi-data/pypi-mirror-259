#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ZhihuZhoukanChengxuRenshengZongdi31Qi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ZhihuZhoukanChengxuRenshengZongdi31Qi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="zhihu-zhoukan-chengxu-rensheng-zongdi-31-qi",
    version=ZhihuZhoukanChengxuRenshengZongdi31Qi.__version__,
    url="https://github.com/apachecn/zhihu-zhoukan-chengxu-rensheng-zongdi-31-qi",
    author=ZhihuZhoukanChengxuRenshengZongdi31Qi.__author__,
    author_email=ZhihuZhoukanChengxuRenshengZongdi31Qi.__email__,
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
    description="知乎周刊·程序人生（总第 31 期）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "zhihu-zhoukan-chengxu-rensheng-zongdi-31-qi=ZhihuZhoukanChengxuRenshengZongdi31Qi.__main__:main",
            "ZhihuZhoukanChengxuRenshengZongdi31Qi=ZhihuZhoukanChengxuRenshengZongdi31Qi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
