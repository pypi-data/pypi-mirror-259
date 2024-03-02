#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import InventionsAndPatentsLectureNotesMit6901
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('InventionsAndPatentsLectureNotesMit6901'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="inventions-and-patents-lecture-notes-mit-6-901",
    version=InventionsAndPatentsLectureNotesMit6901.__version__,
    url="https://github.com/apachecn/inventions-and-patents-lecture-notes-mit-6-901",
    author=InventionsAndPatentsLectureNotesMit6901.__author__,
    author_email=InventionsAndPatentsLectureNotesMit6901.__email__,
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
    description="Inventions and Patents Lecture Notes (MIT 6.901)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "inventions-and-patents-lecture-notes-mit-6-901=InventionsAndPatentsLectureNotesMit6901.__main__:main",
            "InventionsAndPatentsLectureNotesMit6901=InventionsAndPatentsLectureNotesMit6901.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
