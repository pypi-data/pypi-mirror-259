#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import DynamicSystemsAndControlLectureNotesMit6241j
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('DynamicSystemsAndControlLectureNotesMit6241j'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="dynamic-systems-and-control-lecture-notes-mit-6-241j",
    version=DynamicSystemsAndControlLectureNotesMit6241j.__version__,
    url="https://github.com/apachecn/dynamic-systems-and-control-lecture-notes-mit-6-241j",
    author=DynamicSystemsAndControlLectureNotesMit6241j.__author__,
    author_email=DynamicSystemsAndControlLectureNotesMit6241j.__email__,
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
    description="Dynamic Systems and Control Lecture Notes (MIT 6.241J)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "dynamic-systems-and-control-lecture-notes-mit-6-241j=DynamicSystemsAndControlLectureNotesMit6241j.__main__:main",
            "DynamicSystemsAndControlLectureNotesMit6241j=DynamicSystemsAndControlLectureNotesMit6241j.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
