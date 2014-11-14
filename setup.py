#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import business_directory
version = business_directory.__version__

setup(
    name='business_directory',
    version=version,
    author='',
    author_email='michael.mitrofanov@gmail.com',
    packages=[
        'business_directory',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['business_directory/manage.py'],
)