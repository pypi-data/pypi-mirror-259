# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md", encoding="utf-8").read()
except IOError:
    long_description = ""

setup(
    name="huluwa_art",
    version="0.1.0",
    description="A pip package",
    license="MIT",
    author="ocean",
    packages=find_packages(),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)