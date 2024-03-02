#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import JavaSe6LeikuChaxunShouceLongmaGongzuoshi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('JavaSe6LeikuChaxunShouceLongmaGongzuoshi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="java-se-6-leiku-chaxun-shouce-longma-gongzuoshi",
    version=JavaSe6LeikuChaxunShouceLongmaGongzuoshi.__version__,
    url="https://github.com/apachecn/java-se-6-leiku-chaxun-shouce-longma-gongzuoshi",
    author=JavaSe6LeikuChaxunShouceLongmaGongzuoshi.__author__,
    author_email=JavaSe6LeikuChaxunShouceLongmaGongzuoshi.__email__,
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
    description="Java SE 6 类库查询手册（龙马工作室）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "java-se-6-leiku-chaxun-shouce-longma-gongzuoshi=JavaSe6LeikuChaxunShouceLongmaGongzuoshi.__main__:main",
            "JavaSe6LeikuChaxunShouceLongmaGongzuoshi=JavaSe6LeikuChaxunShouceLongmaGongzuoshi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
