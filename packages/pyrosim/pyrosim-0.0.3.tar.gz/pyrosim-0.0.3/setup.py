# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - Intelligentica (Morocco)
Email: a.benmhamed@intelligentica.net
Website: https://intelligentica.net
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyrosim",
    version="0.0.3",
    author="Abdelouahed Ben Mhamed",
    author_email="a.benmhamed@intelligentica.net",
    description="A Python simulator for generating vehicle routing (VRP), capacitated vehicle routing (CVRP) and and drone routing problems (DRP) data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AIM-BENMHAMED/pyrosim",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add any dependencies your library may have
    ]
)
