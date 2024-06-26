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

from steps.inference import infer

"""
Test case for inference.
"""


class TestInference(unittest.TestCase):

    def test_infers_text(self):
        embeddings = infer(
            ["this is testing text"],
            "sentence-transformers/all-MiniLM-L6-v2",
            os.environ["HF_TESTING_TOKEN"]
        )
        frame = pd.DataFrame(embeddings)
        columns = len(frame.columns)
        cexpected = 384
        rows = len(frame)
        rexpected = 1
        self.assertEqual(
            rows,
            rexpected,
            f"Generated embeddings rows count {rows} does not match with expected {rexpected}"
        )
        self.assertEqual(
            columns,
            cexpected,
            f"Generated embeddings columns count {columns} does not match with expected {cexpected}"
        )
