#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Segmentfault2015YouxiuWenzhang
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Segmentfault2015YouxiuWenzhang'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="segmentfault-2015-youxiu-wenzhang",
    version=Segmentfault2015YouxiuWenzhang.__version__,
    url="https://github.com/apachecn/segmentfault-2015-youxiu-wenzhang",
    author=Segmentfault2015YouxiuWenzhang.__author__,
    author_email=Segmentfault2015YouxiuWenzhang.__email__,
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
    description="SegmentFault 2015 优秀文章",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "segmentfault-2015-youxiu-wenzhang=Segmentfault2015YouxiuWenzhang.__main__:main",
            "Segmentfault2015YouxiuWenzhang=Segmentfault2015YouxiuWenzhang.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
