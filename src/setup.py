#!/usr/bin/env python3

from setuptools import setup
from velvet_vista.__version__ import version

setup(
    name="velvet_vista",
    description="Velvet Vista",
    version=version,
    author="Alix",
    author_email="alix@politeauthority.io",
    packages=[
        "velvet_vista",
        "velvet_vista.utils",
        "velvet_vista.modules",
    ],
)

# End File: politeauthority/velvet-vista/src/setup.py
