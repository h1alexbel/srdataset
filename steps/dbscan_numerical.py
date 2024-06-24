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
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN

from steps.members_to_txt import to_txt

frame = pd.read_csv("numerics.csv")
dbscan = DBSCAN(eps=50, min_samples=30)
frame["cluster"] = dbscan.fit_predict(
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
n_clusters = len(set(dbscan.labels_)) - (1 if -1 in dbscan.labels_ else 0)
print(f"Number of clusters found by DBSCAN: {n_clusters}")
to_txt(clusters, "clusters/dbscan/numerical/members")

x_features = [
    "releases", "releases", "releases", "releases", "releases", "releases"
]
y_features = [
    "contributors", "pulls", "commits", "issues", "branches", "workflows"
]

plt.figure(figsize=(10, 8))
colors = plt.get_cmap("tab10", n_clusters)
for x_feature, y_feature in zip(x_features, y_features):
    plt.clf()
    for label in range(n_clusters):
        clustered = frame[frame["cluster"] == label]
        color = colors(label)
        plt.scatter(
            clustered[x_feature],
            clustered[y_feature],
            c=[color],
            label=label,
            marker="o",
            edgecolors="w",
            s=100
        )
    noise = frame[frame["cluster"] == -1]
    plt.scatter(
        noise[x_feature],
        noise[y_feature],
        c='k',
        label='Noise',
        marker="x",
        s=50
    )
    plt.xlabel(x_feature.capitalize())
    plt.ylabel(y_feature.capitalize())
    plt.title(f"DBSCAN Clustering with {n_clusters} Clusters")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"clusters/dbscan/numerical/{x_feature}-vs-{y_feature}.png")
