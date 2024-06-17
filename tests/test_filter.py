# The MIT License (MIT)
#
# Copyright (c) 2024 Aliaksei Bialiauski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import unittest

import pandas as pd

from steps.apply_filter import apply

"""
Test case for Apply Filter.
"""


class TestApplyFilter(unittest.TestCase):

    def tearDown(self):
        os.remove("filtered.csv")

    def test_filters_illegal_repos(self):
        frame = apply("tests/test.csv").reset_index(drop=True)
        expected = pd.read_csv("tests/filter-expected.csv")
        self.assertTrue(
            frame.equals(expected),
            f"Filtered frame {frame} does not match with expected {expected}"
        )

    def test_adds_empty_for_null_topics(self):
        frame = apply("tests/test-with-null-topics.csv").reset_index(drop=True)
        expected = pd.read_csv("tests/filtered-with-null-topics.csv")
        self.assertTrue(
            frame.equals(expected),
            f"Filtered frame {frame} does not match with expected {expected}"
        )
