#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup


setup(
    name = 'bottle-werkzeug',
    version = "0.1.1",
    url = 'https://github.com/bottlepy/bottle-werkzeug',
    description = 'Werkzeug integration for Bottle.',
    long_description = __doc__,
    author = 'Marcel Hellkamp',
    author_email = 'marc@gsites.de',
    license = "MIT",
    platforms = 'any',
    py_modules = [
        'bottle_werkzeug'
    ],
    install_requires = [
        'bottle >= 0.9',
        'werkzeug'
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Bottle'
    ],
)
