#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import PythonJichujiaochengCrossinQuan60Ke
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('PythonJichujiaochengCrossinQuan60Ke'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="python-jichujiaocheng-crossin-quan-60-ke",
    version=PythonJichujiaochengCrossinQuan60Ke.__version__,
    url="https://github.com/apachecn/python-jichujiaocheng-crossin-quan-60-ke",
    author=PythonJichujiaochengCrossinQuan60Ke.__author__,
    author_email=PythonJichujiaochengCrossinQuan60Ke.__email__,
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
    description="Python基础教程(crossin全60课)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "python-jichujiaocheng-crossin-quan-60-ke=PythonJichujiaochengCrossinQuan60Ke.__main__:main",
            "PythonJichujiaochengCrossinQuan60Ke=PythonJichujiaochengCrossinQuan60Ke.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
