#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name='PyCloudNS',
    version='2.0.6',
    description='Python Lib for DNS API on CloudNS.ru',
    long_description=long_description,
    url='http://cloudns.ru',
    author='Vyacheslav Anzhiganov',
    author_email='hello@anzhiganov.com',
    license='MIT',
    # packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages=[
        'PyCloudNS'
    ],
    install_requires=[
        'requests',
    ],
    keywords='public dns service',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
