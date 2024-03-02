#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import CCankaoshouceDierBufen20171220
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('CCankaoshouceDierBufen20171220'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="c-cankaoshouce-dier-bufen-2017-12-20",
    version=CCankaoshouceDierBufen20171220.__version__,
    url="https://github.com/apachecn/c-cankaoshouce-dier-bufen-2017-12-20",
    author=CCankaoshouceDierBufen20171220.__author__,
    author_email=CCankaoshouceDierBufen20171220.__email__,
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
    description="C++ 参考手册 第二部分 2017.12.20",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "c-cankaoshouce-dier-bufen-2017-12-20=CCankaoshouceDierBufen20171220.__main__:main",
            "CCankaoshouceDierBufen20171220=CCankaoshouceDierBufen20171220.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
