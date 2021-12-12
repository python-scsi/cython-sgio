# SPDX-FileCopyrightText: 2020 The cython-sgio Authors
#
# SPDX-License-Identifier: LGPL-2.1-or-later

import sys

# Ensure it's present.
import setuptools_scm  # noqa: F401
from Cython.Build import cythonize
from setuptools import Extension, setup

configured_extensions = []

if sys.platform == "linux":
    configured_extensions.append(Extension("sgio", ["src/linux_sgio.pyx"]))

if not configured_extensions:
    raise NotImplementedError("No SGIO implemented for " + sys.platform)


setup(
    ext_modules=cythonize(configured_extensions),
)
