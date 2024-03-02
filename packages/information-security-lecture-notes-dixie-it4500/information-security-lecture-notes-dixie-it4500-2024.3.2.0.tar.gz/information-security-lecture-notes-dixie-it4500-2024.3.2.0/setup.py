#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import InformationSecurityLectureNotesDixieIt4500
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('InformationSecurityLectureNotesDixieIt4500'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="information-security-lecture-notes-dixie-it4500",
    version=InformationSecurityLectureNotesDixieIt4500.__version__,
    url="https://github.com/apachecn/information-security-lecture-notes-dixie-it4500",
    author=InformationSecurityLectureNotesDixieIt4500.__author__,
    author_email=InformationSecurityLectureNotesDixieIt4500.__email__,
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
    description="Information Security Lecture Notes (Dixie IT4500)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "information-security-lecture-notes-dixie-it4500=InformationSecurityLectureNotesDixieIt4500.__main__:main",
            "InformationSecurityLectureNotesDixieIt4500=InformationSecurityLectureNotesDixieIt4500.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
