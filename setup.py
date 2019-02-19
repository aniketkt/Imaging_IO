#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: atekawade
"""

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Imaging_IO',
    url='https://github.com/aniketkt/Imaging_IO',
    author='Aniket Tekawade',
    author_email='aniketkt@gmail.com',
    # Needed to actually package something
    packages=['Imaging_IO'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='none',
    description='Functions for I/O during image data acquisition.',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
