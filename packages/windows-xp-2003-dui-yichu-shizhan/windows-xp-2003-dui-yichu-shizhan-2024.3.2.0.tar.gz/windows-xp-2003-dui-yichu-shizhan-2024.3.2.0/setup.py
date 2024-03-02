#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import WindowsXp2003DuiYichuShizhan
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('WindowsXp2003DuiYichuShizhan'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="windows-xp-2003-dui-yichu-shizhan",
    version=WindowsXp2003DuiYichuShizhan.__version__,
    url="https://github.com/apachecn/windows-xp-2003-dui-yichu-shizhan",
    author=WindowsXp2003DuiYichuShizhan.__author__,
    author_email=WindowsXp2003DuiYichuShizhan.__email__,
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
    description="Windows XP 2003 堆溢出实战",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "windows-xp-2003-dui-yichu-shizhan=WindowsXp2003DuiYichuShizhan.__main__:main",
            "WindowsXp2003DuiYichuShizhan=WindowsXp2003DuiYichuShizhan.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
