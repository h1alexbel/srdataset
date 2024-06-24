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
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from members_to_txt import to_txt

"""
KMeans clustering with numerical dataset.
"""
frame = pd.read_csv("numerical.csv")
kmeans = KMeans(n_clusters=8, random_state=1)
kmeans.fit(
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
centroids = kmeans.cluster_centers_
print(f"Centeroids: {centroids}")
frame["cluster"] = kmeans.labels_

plt.figure(figsize=(10, 7))
x_features = ["releases", "releases", "releases", "releases", "releases", "releases"]
y_features = ["contributors", "pulls", "commits", "issues", "branches", "workflows"]
for x_feature, y_feature in zip(x_features, y_features):
    plt.clf()
    for cluster in range(8):
        cluster_points = frame[frame["cluster"] == cluster]
        plt.scatter(cluster_points[x_feature], cluster_points[y_feature], label=f'Cluster {cluster}', s=50)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='X', s=100, label='Centroids')
    plt.title(f'K-means Clustering ({x_feature} vs. {y_feature})')
    plt.xlabel(x_feature)
    plt.ylabel(y_feature)
    plt.legend()
    plt.grid(True)
    plt.savefig(f"clusters/kmeans/numerical/{x_feature}-vs-{y_feature}.png")
clusters = frame.groupby('cluster')
to_txt(clusters, "clusters/kmeans/numerical/members")
