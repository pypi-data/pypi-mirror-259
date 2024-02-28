# -*- coding: utf-8 -*-

import shutil

import setuptools
from setuptools.command.install_scripts import install_scripts

from lesscode_address.version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lesscode-address",
    version=__version__,
    author="Chao.yy",
    author_email="yuyc@ishangqi.com",
    description="lesscode-address是处理地址",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/yongchao9/lesscode-address",
    package_data={'': ['dict/*.json', 'dict/*.csv', "cpca/resources/*.csv"]},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    platforms='python',
    install_requires=[
    ]

)
"""
        "aiopg>=1.3.3",
"""
"""
1、打包流程
打包过程中也可以多增加一些额外的操作，减少上传中的错误

# 先升级打包工具
pip install --upgrade setuptools wheel twine

# 打包
python setup.py sdist bdist_wheel

# 检查
twine check dist/*

# 上传pypi
twine upload dist/*
twine upload dist/* -u yuyc -p yu230225
twine upload dist/* --repository-url https://pypi.chanyeos.com/ -u admin -p shangqi
# 安装最新的版本测试
pip install -U lesscode-address -i https://pypi.org/simple
pip install -U lesscode-address -i https://pypi.chanyeos.com/simple
"""
