#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="aukland-compsci-105-problemsolvingwithalgorithmsanddatastructures",
    version=AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures.__version__,
    url="https://github.com/apachecn/aukland-compsci-105-problemsolvingwithalgorithmsanddatastructures",
    author=AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures.__author__,
    author_email=AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures.__email__,
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
    description="Aukland COMPSCI 105 ProblemSolvingwithAlgorithmsandDataStructures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "aukland-compsci-105-problemsolvingwithalgorithmsanddatastructures=AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures.__main__:main",
            "AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures=AuklandCompsci105Problemsolvingwithalgorithmsanddatastructures.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
