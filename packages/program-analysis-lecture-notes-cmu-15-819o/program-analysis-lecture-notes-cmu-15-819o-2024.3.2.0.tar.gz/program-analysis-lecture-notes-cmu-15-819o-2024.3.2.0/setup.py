#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ProgramAnalysisLectureNotesCmu15819o
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ProgramAnalysisLectureNotesCmu15819o'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="program-analysis-lecture-notes-cmu-15-819o",
    version=ProgramAnalysisLectureNotesCmu15819o.__version__,
    url="https://github.com/apachecn/program-analysis-lecture-notes-cmu-15-819o",
    author=ProgramAnalysisLectureNotesCmu15819o.__author__,
    author_email=ProgramAnalysisLectureNotesCmu15819o.__email__,
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
    description="Program Analysis Lecture Notes (CMU 15-819O)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "program-analysis-lecture-notes-cmu-15-819o=ProgramAnalysisLectureNotesCmu15819o.__main__:main",
            "ProgramAnalysisLectureNotesCmu15819o=ProgramAnalysisLectureNotesCmu15819o.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
