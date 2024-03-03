#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="windows-biancheng-rumen-windows-chengxusheji-1-xiaoshi-rumenjiaocheng",
    version=WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng.__version__,
    url="https://github.com/apachecn/windows-biancheng-rumen-windows-chengxusheji-1-xiaoshi-rumenjiaocheng",
    author=WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng.__author__,
    author_email=WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng.__email__,
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
    description="Windows编程入门：Windows程序设计1小时入门教程",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "windows-biancheng-rumen-windows-chengxusheji-1-xiaoshi-rumenjiaocheng=WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng.__main__:main",
            "WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng=WindowsBianchengRumenWindowsChengxusheji1XiaoshiRumenjiaocheng.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
