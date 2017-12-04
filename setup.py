#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name='PyCloudNS',
    version='3.0.0',
    author='Vyacheslav Anzhiganov',
    author_email='hello@anzhiganov.com',
    packages=[
        'PyCloudNS'
    ],
    install_requires=[
        'requests',
    ],
    keywords='public dns service',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
)
