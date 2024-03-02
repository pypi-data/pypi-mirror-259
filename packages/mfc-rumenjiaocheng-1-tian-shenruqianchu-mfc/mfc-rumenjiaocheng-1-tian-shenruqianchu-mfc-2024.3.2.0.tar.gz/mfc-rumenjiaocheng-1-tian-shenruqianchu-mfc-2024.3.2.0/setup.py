#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import MfcRumenjiaocheng1TianShenruqianchuMfc
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('MfcRumenjiaocheng1TianShenruqianchuMfc'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="mfc-rumenjiaocheng-1-tian-shenruqianchu-mfc",
    version=MfcRumenjiaocheng1TianShenruqianchuMfc.__version__,
    url="https://github.com/apachecn/mfc-rumenjiaocheng-1-tian-shenruqianchu-mfc",
    author=MfcRumenjiaocheng1TianShenruqianchuMfc.__author__,
    author_email=MfcRumenjiaocheng1TianShenruqianchuMfc.__email__,
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
    description="MFC入门教程：1天深入浅出MFC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "mfc-rumenjiaocheng-1-tian-shenruqianchu-mfc=MfcRumenjiaocheng1TianShenruqianchuMfc.__main__:main",
            "MfcRumenjiaocheng1TianShenruqianchuMfc=MfcRumenjiaocheng1TianShenruqianchuMfc.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
