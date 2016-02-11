#!/usr/bin/env python

from setuptools import setup

setup(
    name='gaul-django',
    version='1.0.0',
    install_requires=[],
    author='Patrick Dufour',
    author_email='pjdufour.dev@gmail.com',
    license='BSD License',
    url='https://github.com/wfp-ose/gaul-django',
    keywords='python gis wfp gaul',
    description='GAUL, Version 1.x',
    long_description=open('README.rst').read(),
    download_url="https://github.com/wfp-ose/gaul-django/zipball/master",
    packages=[
        "gauldjango",
        "gauldjango.tests"],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
