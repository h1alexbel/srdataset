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
import os
import pandas as pd
from steps.inference import infer

print("Preparing for generating embeddings...")
checkpoint = os.environ["INFERENCE_CHECKPOINT"]
token = os.environ["HF_TOKEN"]
source = "texts"
# @todo #29:45min Generate embeddings for all the text in texts.csv.
#  Some of the texts generated after textualize_repos.py cannot be processed
#  on the embeddings endpoint that lead to raising decoding exception:
#  'json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)'.
#  We should fix that and remove `head(500)` frame limitation.
frame = pd.read_csv(f"{source}.csv").head(500)
candidates = ["text"]
print(f"Checkpoint: {checkpoint}")
print(f"CSV Source: {source}")
print(f"Candidates: {candidates}")

for candidate in candidates:
    print(f"Generating embeddings for {candidate}...")
    embeddings = pd.DataFrame(infer(frame[candidate].tolist(), checkpoint, token))
    embeddings.insert(0, 'repo', frame["repo"])
    embeddings.to_csv(f"{candidate}-embeddings.csv", index=False)
    print(f"Generated embeddings for {candidate}:")
    print(embeddings)
