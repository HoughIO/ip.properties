# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ip.properties',
    version='0.1.0',
    description='A portable flask app to display a user\'s IP address information',
    long_description=readme,
    author='Gorm Houj, Mike Dillion',
    author_email='graham@hough.io, miked@hough.io',
    url='https://github.com/HoughIO/ip.properties',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

