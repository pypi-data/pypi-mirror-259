#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import WeiShengwuXinxixueShejiDePythonJiaocheng
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('WeiShengwuXinxixueShejiDePythonJiaocheng'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="wei-shengwu-xinxixue-sheji-de-python-jiaocheng",
    version=WeiShengwuXinxixueShejiDePythonJiaocheng.__version__,
    url="https://github.com/apachecn/wei-shengwu-xinxixue-sheji-de-python-jiaocheng",
    author=WeiShengwuXinxixueShejiDePythonJiaocheng.__author__,
    author_email=WeiShengwuXinxixueShejiDePythonJiaocheng.__email__,
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
    description="为生物信息学设计的Python教程",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "wei-shengwu-xinxixue-sheji-de-python-jiaocheng=WeiShengwuXinxixueShejiDePythonJiaocheng.__main__:main",
            "WeiShengwuXinxixueShejiDePythonJiaocheng=WeiShengwuXinxixueShejiDePythonJiaocheng.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
