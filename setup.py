#!/usr/bin/env python

import hackNews
import os
from setuptools import setup, find_packages

setup(
    name='hackNews',
    version=hackNews.__version__,
    description='Command line utility to access the Hacker News website in a more fun/useful way',
    author='Deep Aggarwal',
    author_email='deep.uiuc@gmail.com',
    maintainer='Deep Aggarwal',
    maintainer_email='deep.uiuc@gmail.com',
    url='https://github.com/deep4788/hackTechNews',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hackNews = hackNews.hackNews:main',
        ]
    },
)
