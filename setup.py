#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='shiphawk-client-python',
    version='0.0.3',
    description='ShipHawk API Client for Python',
    author='Douglas Treadwell',
    author_email='douglas.treadwell@gmail.com',
    url='https://github.com/Distribute-Inc/shiphawk-client-python',
    packages=['shiphawk', 'shiphawk.api'],
    install_requires=[
        'requests[security] >= 2.11.1'
    ]
)
