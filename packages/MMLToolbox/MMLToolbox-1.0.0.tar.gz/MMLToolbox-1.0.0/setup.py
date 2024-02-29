#!/usr/bin/env python

from distutils.core import setup

setup(
    name="MMLToolbox",
    version="1.0.0",
    description="",
    author="IGTE",
    author_email="andreas.gschwentner@tugraz.at",
    url="https://www.tugraz.at/institute/igte/home/",
    packages=["MMLToolbox", "MMLToolbox.util", "MMLToolbox.coord", "MMLToolbox.optic", "MMLToolbox.pxi"],
    # include_package_data=True,
    # scripts=["bin/generate-ex"],
    keywords=["parameter", "identification", "measurements", "optimization"],
    install_requires=["numpy", ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    )
