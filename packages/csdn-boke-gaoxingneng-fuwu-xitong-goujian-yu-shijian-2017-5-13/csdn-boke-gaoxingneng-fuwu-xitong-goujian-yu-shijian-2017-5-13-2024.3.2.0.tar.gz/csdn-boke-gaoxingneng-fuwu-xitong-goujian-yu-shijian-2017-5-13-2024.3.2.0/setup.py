#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="csdn-boke-gaoxingneng-fuwu-xitong-goujian-yu-shijian-2017-5-13",
    version=CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513.__version__,
    url="https://github.com/apachecn/csdn-boke-gaoxingneng-fuwu-xitong-goujian-yu-shijian-2017-5-13",
    author=CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513.__author__,
    author_email=CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513.__email__,
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
    description="CSDN 博客 - 高性能服务系统构建与实践 2017.5.13",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "csdn-boke-gaoxingneng-fuwu-xitong-goujian-yu-shijian-2017-5-13=CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513.__main__:main",
            "CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513=CsdnBokeGaoxingnengFuwuXitongGoujianYuShijian2017513.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
