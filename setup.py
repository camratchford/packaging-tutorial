#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup, find_packages


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    path = os.path.join(package, "__init__.py")
    init_py = open(path, "r", encoding="utf8").read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description():
    """
    Return the README.
    """
    return open("README.md", "r", encoding="utf8").read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


env_marker_cpython = (
    "sys_platform != 'win32'"
    " and (sys_platform != 'cygwin'"
    " and platform_python_implementation != 'PyPy')"
)

env_marker_win = "sys_platform == 'win32'"
env_marker_below_38 = "python_version < '3.8'"

minimal_requirements = [
    "click==8.1.3",
    "colorama==0.4.6",
    "PyYAML==6.0"
]


extra_requirements = [
    "uvloop>=0.14.0,!=0.15.0,!=0.15.1; " + env_marker_cpython,
    "colorama>=0.4;" + env_marker_win,
]


setup(
    name="Packaging Tutorial",
    version="0.0.1",
    url="https://github.com/camratchford/packaging_tutorial",
    license="CC0 1.0 Universal",
    description="A quick tour of how to set up a Python package",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Cam Ratchford",
    author_email="cameron@ratchfordconsulting.com",
    packages=get_packages('packaging_tut'),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=minimal_requirements,
    extras_require={"standard": extra_requirements},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Administrators",
        "License :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        'console_scripts': {
            'packaging_tut = packaging_tut.cli:run',
        }
    },
    project_urls={
        "Funding": "https://github.com/sponsors/camratchford",
        "Source": "https://github.com/camratchford/packaging_tutorial",
        "Changelog": "https://github.com/camratchford/packaging_tutorial/blob/master/CHANGELOG.md",
    },
)