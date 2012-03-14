#!/usr/bin/env python
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='lastfm importer',
    version='0.1',
    description='',
    author='alswl',
    author_email='alswl@gmail.com',
    url='http://log4d.com',
    requires=[
        'cElementTree',
        'eyeD3'
    ],
)
