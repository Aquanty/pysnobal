#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pysnobal
----------------------------------

Tests for `pysnobal` module.
"""

import unittest

from pysnobal.c_snobal import snobal


class TestPysnobal(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        self.assertTrue(hasattr(snobal, "do_tstep_grid"))


if __name__ == "__main__":
    unittest.main()
