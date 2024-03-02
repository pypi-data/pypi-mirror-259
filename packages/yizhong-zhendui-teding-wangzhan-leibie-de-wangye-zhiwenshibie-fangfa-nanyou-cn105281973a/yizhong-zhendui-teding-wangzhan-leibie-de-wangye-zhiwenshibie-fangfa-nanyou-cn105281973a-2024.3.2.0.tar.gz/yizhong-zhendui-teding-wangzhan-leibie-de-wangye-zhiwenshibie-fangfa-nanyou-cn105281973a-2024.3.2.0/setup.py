#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="yizhong-zhendui-teding-wangzhan-leibie-de-wangye-zhiwenshibie-fangfa-nanyou-cn105281973a",
    version=YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a.__version__,
    url="https://github.com/apachecn/yizhong-zhendui-teding-wangzhan-leibie-de-wangye-zhiwenshibie-fangfa-nanyou-cn105281973a",
    author=YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a.__author__,
    author_email=YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a.__email__,
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
    description="一种针对特定网站类别的网页指纹识别方法 （南邮 CN105281973A）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "yizhong-zhendui-teding-wangzhan-leibie-de-wangye-zhiwenshibie-fangfa-nanyou-cn105281973a=YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a.__main__:main",
            "YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a=YizhongZhenduiTedingWangzhanLeibieDeWangyeZhiwenshibieFangfaNanyouCn105281973a.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
