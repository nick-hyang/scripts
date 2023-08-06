"""
@Note: 
@Author: yang hui
@Date: 2023/8/6 21:09
"""
from setuptools import setup, find_packages

# 项目信息
NAME = 'scripts'
VERSION = '0.1.0'
DESCRIPTION = 'scripts collection'
AUTHOR = 'Nick'
EMAIL = 'nick@example.com'
URL = 'https://github.com/your_username/your_package'
LICENSE = 'MIT'

# 项目依赖
INSTALL_REQUIRES = [
    # 依赖包列表
]

# 项目入口点
ENTRY_POINTS = {
    # 'console_scripts': [
    #     'your_command = your_package.module:function_to_execute',
    # ]
}

# 读取 README 文件内容作为 long_description
with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=LICENSE,
    packages=find_packages(exclude=['tests']),
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

