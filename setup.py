# SPDX-FileCopyrightText: 2020 The cython-sgio Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later

import sys

from setuptools import Extension, find_packages, setup

# Ensure it's present.
import setuptools_scm  # noqa: F401
from Cython.Build import cythonize

configured_extensions = []

if sys.platform == "linux":
    configured_extensions.append(Extension("sgio", ["src/linux_sgio.pyx"]))

if not configured_extensions:
    raise NotImplementedError("No SGIO implemented for " + sys.platform)


setup(
    packages=find_packages(),
    package_data={"": ["*.pyx", "*.pxd"]},
    ext_modules=cythonize(configured_extensions),
    extras_require={
        "dev": [
            "Cython",
            "mypy",
            "pre-commit",
            "setuptools>=42",
            "setuptools_scm[toml]>=3.4",
            "wheel",
        ]
    },
)
