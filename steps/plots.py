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
from matplotlib import pyplot as plt

"""
Create plots.
"""


class Plots:
    def __init__(self, frame, n_clusters):
        self.frame = frame
        self.n_clusters = n_clusters

    def plot(self, x_features, y_features, prefix):
        plt.figure(figsize=(10, 8))
        colors = plt.get_cmap("tab10", self.n_clusters)
        for x_feature, y_feature in zip(x_features, y_features):
            plt.clf()
            for label in range(self.n_clusters):
                clustered = self.frame[self.frame["cluster"] == label]
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
            plt.xlabel(x_feature.capitalize())
            plt.ylabel(y_feature.capitalize())
            plt.title(f"Clustering with {self.n_clusters} Clusters")
            plt.legend()
            plt.tight_layout()
            plt.savefig(f"{prefix}/{x_feature}-vs-{y_feature}.png")
