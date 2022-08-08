#!/usr/bin/env python3

from setuptools import setup

setup(name="search-handler-flask",
    version="1.0",
    long_description=__doc__,
    packages=["search-handler"],
    include_package_data=True,
    zip_safe=False,
    install_requires=["Flask", "Waitress"])
