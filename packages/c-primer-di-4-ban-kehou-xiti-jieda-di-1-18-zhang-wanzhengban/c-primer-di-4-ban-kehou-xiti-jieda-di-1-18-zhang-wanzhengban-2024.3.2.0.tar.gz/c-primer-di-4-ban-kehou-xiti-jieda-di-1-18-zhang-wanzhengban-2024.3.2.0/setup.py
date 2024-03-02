#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="c-primer-di-4-ban-kehou-xiti-jieda-di-1-18-zhang-wanzhengban",
    version=CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban.__version__,
    url="https://github.com/apachecn/c-primer-di-4-ban-kehou-xiti-jieda-di-1-18-zhang-wanzhengban",
    author=CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban.__author__,
    author_email=CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban.__email__,
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
    description="C++Primer第4版课后习题解答(第1-18章)完整版",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "c-primer-di-4-ban-kehou-xiti-jieda-di-1-18-zhang-wanzhengban=CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban.__main__:main",
            "CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban=CPrimerDi4BanKehouXitiJiedaDi118ZhangWanzhengban.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
