#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Pyqt4JingcaiShiliFenxi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Pyqt4JingcaiShiliFenxi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="pyqt4-jingcai-shili-fenxi",
    version=Pyqt4JingcaiShiliFenxi.__version__,
    url="https://github.com/apachecn/pyqt4-jingcai-shili-fenxi",
    author=Pyqt4JingcaiShiliFenxi.__author__,
    author_email=Pyqt4JingcaiShiliFenxi.__email__,
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
    description="PyQt4 精彩实例分析",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "pyqt4-jingcai-shili-fenxi=Pyqt4JingcaiShiliFenxi.__main__:main",
            "Pyqt4JingcaiShiliFenxi=Pyqt4JingcaiShiliFenxi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
