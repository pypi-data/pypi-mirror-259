#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import LinuxNeihe011WanquanZhushiXiuzhengbanV195
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('LinuxNeihe011WanquanZhushiXiuzhengbanV195'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="linux-neihe-0-11-wanquan-zhushi-xiuzhengban-v1-9-5",
    version=LinuxNeihe011WanquanZhushiXiuzhengbanV195.__version__,
    url="https://github.com/apachecn/linux-neihe-0-11-wanquan-zhushi-xiuzhengban-v1-9-5",
    author=LinuxNeihe011WanquanZhushiXiuzhengbanV195.__author__,
    author_email=LinuxNeihe011WanquanZhushiXiuzhengbanV195.__email__,
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
    description="Linux内核0.11完全注释(修正版v1.9.5)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "linux-neihe-0-11-wanquan-zhushi-xiuzhengban-v1-9-5=LinuxNeihe011WanquanZhushiXiuzhengbanV195.__main__:main",
            "LinuxNeihe011WanquanZhushiXiuzhengbanV195=LinuxNeihe011WanquanZhushiXiuzhengbanV195.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
