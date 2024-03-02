#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import DeeplearningaiBijiV51HuanghaiGuang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('DeeplearningaiBijiV51HuanghaiGuang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="deeplearningai-biji-v5-1-huanghai-guang",
    version=DeeplearningaiBijiV51HuanghaiGuang.__version__,
    url="https://github.com/apachecn/deeplearningai-biji-v5-1-huanghai-guang",
    author=DeeplearningaiBijiV51HuanghaiGuang.__author__,
    author_email=DeeplearningaiBijiV51HuanghaiGuang.__email__,
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
    description="DeepLearningAI 笔记 v5.1（黄海广）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "deeplearningai-biji-v5-1-huanghai-guang=DeeplearningaiBijiV51HuanghaiGuang.__main__:main",
            "DeeplearningaiBijiV51HuanghaiGuang=DeeplearningaiBijiV51HuanghaiGuang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
