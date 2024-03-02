#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="caffe-guanfang-jiaocheng-zhongyiben-caffecn-shequ-fanyi",
    version=CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi.__version__,
    url="https://github.com/apachecn/caffe-guanfang-jiaocheng-zhongyiben-caffecn-shequ-fanyi",
    author=CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi.__author__,
    author_email=CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi.__email__,
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
    description="Caffe官方教程中译本 CaffeCN社区翻译",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "caffe-guanfang-jiaocheng-zhongyiben-caffecn-shequ-fanyi=CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi.__main__:main",
            "CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi=CaffeGuanfangJiaochengZhongyibenCaffecnShequFanyi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
