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
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from members_to_txt import to_txt
from steps.plots import Plots

"""
Agglomerative clustering on numerical dataset.
"""

frame = pd.read_csv("numerical.csv.csv")
n_clusters = 6
agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
frame["cluster"] = agglomerative.fit_predict(
    frame[
        [
            "releases",
            "contributors",
            "pulls",
            "commits",
            "issues",
            "branches",
            "workflows"
        ]
    ]
)
clusters = frame.groupby("cluster")
to_txt(clusters, "clusters/agglomerative/numerical/members")

Plots(frame, n_clusters).plot(
    x_features=[
        "releases", "releases", "releases", "releases", "releases", "releases"
    ],
    y_features=[
        "contributors", "pulls", "commits", "issues", "branches", "workflows"
    ],
    prefix="clusters/agglomerative/numerical"
)
