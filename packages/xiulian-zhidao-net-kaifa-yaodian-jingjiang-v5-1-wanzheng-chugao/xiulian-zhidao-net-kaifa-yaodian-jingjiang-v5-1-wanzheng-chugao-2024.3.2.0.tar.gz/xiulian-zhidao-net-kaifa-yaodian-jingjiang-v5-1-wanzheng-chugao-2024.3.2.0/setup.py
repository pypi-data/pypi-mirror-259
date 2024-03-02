#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xiulian-zhidao-net-kaifa-yaodian-jingjiang-v5-1-wanzheng-chugao",
    version=XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao.__version__,
    url="https://github.com/apachecn/xiulian-zhidao-net-kaifa-yaodian-jingjiang-v5-1-wanzheng-chugao",
    author=XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao.__author__,
    author_email=XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao.__email__,
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
    description="修炼之道：.NET开发要点精讲V5.1(完整初稿)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xiulian-zhidao-net-kaifa-yaodian-jingjiang-v5-1-wanzheng-chugao=XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao.__main__:main",
            "XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao=XiulianZhidaoNetKaifaYaodianJingjiangV51WanzhengChugao.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
