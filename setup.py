# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample Project',
    long_description=readme,
    author='Gorm Houj',
    author_email='graham@hough.io',
    url='https://github.com/HoughIO/templates',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

