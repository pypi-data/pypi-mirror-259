#!/usr/bin/env python

from setuptools import setup, find_packages
from learntester import VERSION

url = "https://github.com/kathjade/learntester"

long_description = "virtual coin & task management for mobile app (specially for indonesia)"

setup(
    name="learntester",
    version=VERSION,
    description=long_description,
    maintainer="kath jade",
    maintainer_email="kathjade315@gmail.com",
    url=url,
    long_description=long_description,
    packages=find_packages('.'),
    zip_safe=False,
    install_requires=[
        'requests',
        'wechat',
        'youchat',
        'jsonfield',
        'youhat',
        'simplejson',
        'dicttoxml',
        'xmltodict',
    ]
)
