#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import R4ndomPojieJiaochengFanyi120aByQqsniper
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('R4ndomPojieJiaochengFanyi120aByQqsniper'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="r4ndom-pojie-jiaocheng-fanyi-1-20a-by-qqsniper",
    version=R4ndomPojieJiaochengFanyi120aByQqsniper.__version__,
    url="https://github.com/apachecn/r4ndom-pojie-jiaocheng-fanyi-1-20a-by-qqsniper",
    author=R4ndomPojieJiaochengFanyi120aByQqsniper.__author__,
    author_email=R4ndomPojieJiaochengFanyi120aByQqsniper.__email__,
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
    description="R4ndom 破解教程翻译 1~20a by QQSniper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "r4ndom-pojie-jiaocheng-fanyi-1-20a-by-qqsniper=R4ndomPojieJiaochengFanyi120aByQqsniper.__main__:main",
            "R4ndomPojieJiaochengFanyi120aByQqsniper=R4ndomPojieJiaochengFanyi120aByQqsniper.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
