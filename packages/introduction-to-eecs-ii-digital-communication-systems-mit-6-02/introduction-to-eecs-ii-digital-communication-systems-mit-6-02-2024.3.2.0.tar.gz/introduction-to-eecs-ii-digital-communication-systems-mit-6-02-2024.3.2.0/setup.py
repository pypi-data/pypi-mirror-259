#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import IntroductionToEecsIiDigitalCommunicationSystemsMit602
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('IntroductionToEecsIiDigitalCommunicationSystemsMit602'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="introduction-to-eecs-ii-digital-communication-systems-mit-6-02",
    version=IntroductionToEecsIiDigitalCommunicationSystemsMit602.__version__,
    url="https://github.com/apachecn/introduction-to-eecs-ii-digital-communication-systems-mit-6-02",
    author=IntroductionToEecsIiDigitalCommunicationSystemsMit602.__author__,
    author_email=IntroductionToEecsIiDigitalCommunicationSystemsMit602.__email__,
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
    description="Introduction to EECS II Digital Communication Systems (MIT 6.02)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "introduction-to-eecs-ii-digital-communication-systems-mit-6-02=IntroductionToEecsIiDigitalCommunicationSystemsMit602.__main__:main",
            "IntroductionToEecsIiDigitalCommunicationSystemsMit602=IntroductionToEecsIiDigitalCommunicationSystemsMit602.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
