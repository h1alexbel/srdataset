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
import torch
from sentence_transformers.util import semantic_search

from steps.inference import infer

"""
Find similar text to the head.
"""


def similar(dimension, head):
    embeddings = pd.read_csv(f"{dimension}-embeddings.csv")
    dataset = torch.from_numpy(embeddings.to_numpy()).to(torch.float)
    head_embeddings = torch.FloatTensor(
        infer([head], os.environ["INFERENCE_CHECKPOINT"], os.environ["HF_TOKEN"])
    )
    hits = semantic_search(head_embeddings, dataset, top_k=5)
    frame = pd.read_csv(f"{os.environ['CSV']}.csv")
    return [frame[dimension][hits[0][i]['corpus_id']] for i in range(len(hits[0]))]
