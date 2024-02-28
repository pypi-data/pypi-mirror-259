#!/usr/bin/env python
#
# Copyright (c) 2020-2024 PigeonsAI Inc. All right reserved.
#

import os
from setuptools import setup, find_packages


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), encoding="utf-8") as f:
        return f.read()


long_desc = """build production ready machine learning applications."""

setup(
    name="tensorstack",
    version="0.0.0.1",
    description="client and SDK",
    license="Proprietary License",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="PigeonsAI Inc.",
    author_email="info@pigeonsai.com",
    keywords="",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read("requirements.txt"),
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology"
    ]
)
