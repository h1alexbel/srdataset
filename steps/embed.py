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
import requests

print("Preparing for generating embeddings...")
checkpoint = "sentence-transformers/all-MiniLM-L6-v2"
token = os.environ["HF_TOKEN"]
source = "filtered.csv"
frame = pd.read_csv(source)
candidates = ["description", "readme", "topics"]
print(f"Checkpoint: {checkpoint}")
print(f"CSV Source: {source}")
print(f"Candidates: {candidates}")


def query(texts):
    return requests.post(
        f"https://api-inference.huggingface.co/pipeline/feature-extraction/{checkpoint}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "inputs": texts,
            "options": {
                "wait_for_model": True
            }
        }
    ).json()


for candidate in candidates:
    print(f"Generating embeddings for {candidate}...")
    embeddings = pd.DataFrame(query(frame[candidate].tolist()))
    embeddings.to_csv(f"{candidate}-embeddings.csv", index=False)
    print(f"Generated embeddings for {candidate}:")
    print(embeddings)
