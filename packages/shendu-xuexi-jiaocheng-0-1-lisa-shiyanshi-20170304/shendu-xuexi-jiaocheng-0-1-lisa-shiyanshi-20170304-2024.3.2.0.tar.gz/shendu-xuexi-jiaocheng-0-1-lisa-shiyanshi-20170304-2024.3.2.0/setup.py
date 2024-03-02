#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import ShenduXuexiJiaocheng01LisaShiyanshi20170304
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('ShenduXuexiJiaocheng01LisaShiyanshi20170304'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="shendu-xuexi-jiaocheng-0-1-lisa-shiyanshi-20170304",
    version=ShenduXuexiJiaocheng01LisaShiyanshi20170304.__version__,
    url="https://github.com/apachecn/shendu-xuexi-jiaocheng-0-1-lisa-shiyanshi-20170304",
    author=ShenduXuexiJiaocheng01LisaShiyanshi20170304.__author__,
    author_email=ShenduXuexiJiaocheng01LisaShiyanshi20170304.__email__,
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
    description="深度学习教程 0.1（LISA 实验室）20170304",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "shendu-xuexi-jiaocheng-0-1-lisa-shiyanshi-20170304=ShenduXuexiJiaocheng01LisaShiyanshi20170304.__main__:main",
            "ShenduXuexiJiaocheng01LisaShiyanshi20170304=ShenduXuexiJiaocheng01LisaShiyanshi20170304.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
