#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import numpy

from setuptools import find_packages, setup, Extension

from Cython.Distutils import build_ext

# ------------------------------------------------------------------------------
# Compiling the C code for the Snobal library

c_sources = glob.glob(os.path.join("pysnobal", "c_snobal", "libsnobal", "*.c"))
extra_cc_args = ["-fopenmp", "-O3", "-L./pysnobal", "-ggdb3"]
extensions = [
    Extension(
        "pysnobal.c_snobal.snobal",
        sources=c_sources + ["pysnobal/c_snobal/snobal.pyx"],
        # libraries=["snobal"],
        include_dirs=[numpy.get_include(), "pysnobal/c_snobal", "pysnobal/c_snobal/h"],
        # runtime_library_dirs=['{}'.format(os.path.join(cwd,'pysnobal'))],
        extra_compile_args=extra_cc_args,
        extra_link_args=extra_cc_args,
    )
]

setup(
    packages=find_packages(exclude=["tests"]),
    ext_modules=extensions,
    include_package_data=True,
)
