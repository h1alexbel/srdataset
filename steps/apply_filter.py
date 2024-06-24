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
import pandas as pd
from langdetect import DetectorFactory

from steps.english import english
from steps.md_to_text import to_text

"""
Apply filtering on a CSV file.
"""


def apply(csv):
    print("Start filtering...")
    DetectorFactory.seed = 0
    frame = pd.read_csv(csv)
    start = len(frame)
    print(f"Repositories in: {start}")
    frame["topics"] = frame["topics"].fillna("[]")
    frame = frame.dropna(subset=["readme", "description"])
    skipped = start - len(frame)
    after_null = len(frame)
    print(f"Skipped {skipped} repositories with NULL in rows")
    frame = frame[frame["description"].apply(english)]
    frame["readme"] = frame["readme"].apply(to_text)
    frame = frame[frame["readme"].apply(english)]
    frame = frame.dropna(subset=["readme"])
    skipped_non_english = after_null - len(frame)
    print(f"Skipped {skipped_non_english} non-english repositories")
    print(f"Total skipped: {skipped + skipped_non_english}")
    print(f"Staying with {len(frame)} good repositories")
    print(frame)
    return frame
