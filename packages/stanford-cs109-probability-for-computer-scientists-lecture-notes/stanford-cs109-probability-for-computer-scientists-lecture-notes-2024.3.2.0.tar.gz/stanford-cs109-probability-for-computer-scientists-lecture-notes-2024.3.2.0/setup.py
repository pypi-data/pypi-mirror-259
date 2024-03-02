#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import StanfordCs109ProbabilityForComputerScientistsLectureNotes
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('StanfordCs109ProbabilityForComputerScientistsLectureNotes'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="stanford-cs109-probability-for-computer-scientists-lecture-notes",
    version=StanfordCs109ProbabilityForComputerScientistsLectureNotes.__version__,
    url="https://github.com/apachecn/stanford-cs109-probability-for-computer-scientists-lecture-notes",
    author=StanfordCs109ProbabilityForComputerScientistsLectureNotes.__author__,
    author_email=StanfordCs109ProbabilityForComputerScientistsLectureNotes.__email__,
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
    description="Stanford CS109 Probability for Computer Scientists Lecture Notes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "stanford-cs109-probability-for-computer-scientists-lecture-notes=StanfordCs109ProbabilityForComputerScientistsLectureNotes.__main__:main",
            "StanfordCs109ProbabilityForComputerScientistsLectureNotes=StanfordCs109ProbabilityForComputerScientistsLectureNotes.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
