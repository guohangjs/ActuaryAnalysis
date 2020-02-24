# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:24:21 2020

@author: Hang Guo
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ActuaryAnalysis", # Replace with your own username
    version="0.0.1",
    author="Hang Guo",
    author_email="guohangjs@foxmail.com",
    description="Python package for actuaries to analyze actuarial problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guohangjs/ActuaryAnalysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)