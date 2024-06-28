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
import unittest
import pytest
from langdetect import DetectorFactory

from steps.english import english

"""
Test case for English.
"""


class TestSkipNonEnglish(unittest.TestCase):

    def test_detects_eng(self):
        text = "Testing testing testing"
        self.assertTrue(
            english(text),
            f"input text ({text}) is not in english, but should be"
        )

    def test_returns_false_on_chinese(self):
        text = "一个轻量级 Java 权限认证框架"
        self.assertFalse(
            english(text),
            f"input text {text} is english, but should not be"
        )

    def test_returns_false_on_failures(self):
        text = ""
        self.assertFalse(
            english(text),
            f"input text {text} is english, but should not be"
        )

    # @todo #29:30min Language detection produces inaccurate results for mixed
    #  language text. We should fix that in order to filter out more
    #  repositories with non-english texts. Don't forget to remove this puzzle.
    @pytest.mark.skip
    def test_returns_false_on_mixed(self):
        text = ("clash节点、免费clash节点、免费节点、免费梯子、clash科学上网、clash翻墙、clash订阅链接、clash for "
                "Windows、clash教程、免费公益节点、最新clash免费节点订阅地址、clash免费节点每日更新")
        self.assertFalse(
            english(text),
            f"input text {text} is english, but should not be"
        )

    def test_returns_false_on_prepared_chinese(self):
        DetectorFactory.seed = 0
        with open("tests/cn-prepared.txt") as f: content = f.read()
        self.assertFalse(
            english(content),
            f"input text {content} is english, but should not be"
        )
