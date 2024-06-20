#!/usr/bin/env python3
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

"""
Similarity between repository dimensions.
"""
import pandas as pd
from steps.similar import similar

heads = [
    """
streaming-with-flink/examples-java;Java Examples for Stream Processing with Apache Flink
This repository hosts Java code examples for Stream Processing with Apache Flink by Fabian Hueske.
Note: The Java examples are not comlete yet. The Scala examples are complete and we are working
on translating them to Java.;Stream Processing with Apache Flink - Java Examples;awesome, java
    """
]
dimension = "text"
similarities = []
for head in heads:
    similarity = {
        "head": head,
        "dimension": dimension,
        "similar": " ".join(similar(dimension, head, "texts.csv"))
    }
    similarities.append(similarity)
frame = pd.DataFrame(similarities).to_csv("similar.csv", index=False)
