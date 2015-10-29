#!/usr/bin/env python

from setuptools import setup

setup(
    name='scikit-gof',
    version='0.0.1',
    packages=('skgof',),
    install_requires=('numpy>=1.10', 'scipy'),
    tests_require=('pytest', 'pytest-flake8', 'pytest-isort', 'pytest-readme',
                   'flake8-print', 'flake8-todo', 'pep8-naming'),

    description="Variations on goodness of fit tests for SciPy.",
    author="Wojciech Ruszczewski",
    author_email="scipy@wr.waw.pl",
    url="http://github.org/wrwrwr/scikit-gof",
    license="MIT",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
    ),
)