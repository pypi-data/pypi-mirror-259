#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xuexi-ionic-shiyong-ionic-goujian-shishi-hunhe-yidong-yingyong-chugao",
    version=XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao.__version__,
    url="https://github.com/apachecn/xuexi-ionic-shiyong-ionic-goujian-shishi-hunhe-yidong-yingyong-chugao",
    author=XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao.__author__,
    author_email=XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao.__email__,
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
    description="学习Ionic - 使用Ionic构建实时混合移动应用（初稿）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xuexi-ionic-shiyong-ionic-goujian-shishi-hunhe-yidong-yingyong-chugao=XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao.__main__:main",
            "XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao=XuexiIonicShiyongIonicGoujianShishiHunheYidongYingyongChugao.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
