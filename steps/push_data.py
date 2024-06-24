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

from huggingface_hub import HfApi

"""
Push outputs to the HuggingFace datasets.
"""

outputs = [
    "repos",
    "filtered",
    "texts",
    "text-embeddings",
    "similar",
    "numerical"
]

if os.environ["PUSH_TO_HF"]:
    profile = os.environ["HF_PROFILE"]
    print(f"Pushing outputs: {outputs}, since PUSH_HF is true.")
    api = HfApi()
    for output in outputs:
        path = f"{profile}/sr-{output}"
        if not api.repo_exists(path, repo_type="dataset"):
            api.create_repo(
                repo_id=path,
                repo_type="dataset"
            )
        api.upload_file(
            path_or_fileobj=f"{output}.csv",
            path_in_repo=f"preprocessed/{output}.csv",
            repo_id=f"h1alexbel/sr-{output}",
            repo_type="dataset"
        )
