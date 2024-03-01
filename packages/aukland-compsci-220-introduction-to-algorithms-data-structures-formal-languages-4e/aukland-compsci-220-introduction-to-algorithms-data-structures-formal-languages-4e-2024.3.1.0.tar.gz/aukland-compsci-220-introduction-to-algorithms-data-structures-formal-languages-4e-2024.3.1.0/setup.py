#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="aukland-compsci-220-introduction-to-algorithms-data-structures-formal-languages-4e",
    version=AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e.__version__,
    url="https://github.com/apachecn/aukland-compsci-220-introduction-to-algorithms-data-structures-formal-languages-4e",
    author=AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e.__author__,
    author_email=AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e.__email__,
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
    description="Aukland COMPSCI 220 Introduction to Algorithms, Data Structures & Formal Languages 4e",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "aukland-compsci-220-introduction-to-algorithms-data-structures-formal-languages-4e=AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e.__main__:main",
            "AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e=AuklandCompsci220IntroductionToAlgorithmsDataStructuresFormalLanguages4e.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
