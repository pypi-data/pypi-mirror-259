#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import TtAnquanXinxianquanRenyuanCongyeZhinan
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('TtAnquanXinxianquanRenyuanCongyeZhinan'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="tt-anquan-xinxianquan-renyuan-congye-zhinan",
    version=TtAnquanXinxianquanRenyuanCongyeZhinan.__version__,
    url="https://github.com/apachecn/tt-anquan-xinxianquan-renyuan-congye-zhinan",
    author=TtAnquanXinxianquanRenyuanCongyeZhinan.__author__,
    author_email=TtAnquanXinxianquanRenyuanCongyeZhinan.__email__,
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
    description="TT 安全 信息安全人员从业指南",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "tt-anquan-xinxianquan-renyuan-congye-zhinan=TtAnquanXinxianquanRenyuanCongyeZhinan.__main__:main",
            "TtAnquanXinxianquanRenyuanCongyeZhinan=TtAnquanXinxianquanRenyuanCongyeZhinan.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
