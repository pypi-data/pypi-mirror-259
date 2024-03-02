#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="the-art-of-approximation-in-science-and-engineering-lecture-notes-mit-6-055j",
    version=TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j.__version__,
    url="https://github.com/apachecn/the-art-of-approximation-in-science-and-engineering-lecture-notes-mit-6-055j",
    author=TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j.__author__,
    author_email=TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j.__email__,
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
    description="The Art of Approximation in Science and Engineering Lecture Notes (MIT 6.055J)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "the-art-of-approximation-in-science-and-engineering-lecture-notes-mit-6-055j=TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j.__main__:main",
            "TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j=TheArtOfApproximationInScienceAndEngineeringLectureNotesMit6055j.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
