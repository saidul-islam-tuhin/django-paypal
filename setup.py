#!/usr/bin/env python

import os.path

from setuptools import find_packages, setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

DESCRIPTION = 'A pluggable Django application for integrating PayPal Payments Standard or Payments Pro'
URL = 'https://github.com/spookylukey/django-paypal'
DOCS_URL = 'https://django-paypal.readthedocs.org'

setup(
    name='django-paypal',
    version="0.5.1.dev1",
    author='John Boxall',
    author_email='john@handimobility.ca',
    maintainer="Luke Plant",
    maintainer_email="L.Plant.98@cantab.net",
    url=URL,
    install_requires=[
        'Django>=1.6',
        'six>=1.4.1',
        'requests>=2.5.3',
        'pytz>=2015.4',
    ],
    description=DESCRIPTION,
    long_description="%s\n\nHome page: %s\n\nDocs: %s\n" % (DESCRIPTION, URL, DOCS_URL),
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
