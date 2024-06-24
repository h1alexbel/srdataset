import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

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
to_txt(clusters, "clusters/dbscan/numerical/members")

# pca = PCA(n_components=2)
# principal_components = pca.fit_transform(frame[["releases", "contributors", "pulls", "commits", "issues", "branches", "workflows"]])
# frame['pca1'] = principal_components[:, 0]
# frame['pca2'] = principal_components[:, 1]
#
# plt.figure(figsize=(10, 8))
# unique_labels = frame['cluster'].unique()
# colors = plt.get_cmap("tab10", len(unique_labels))
#
# for cluster_label in unique_labels:
#     clustered_data = frame[frame['cluster'] == cluster_label]
#     color = 'k' if cluster_label == -1 else colors(cluster_label)
#     label = 'Noise' if cluster_label == -1 else f'Cluster {cluster_label}'
#     plt.scatter(clustered_data['pca1'], clustered_data['pca2'], c=[color], label=label, marker='o', edgecolors='w', s=100)
#
# plt.xlabel('PCA Component 1')
# plt.ylabel('PCA Component 2')
# plt.title('DBSCAN Clustering Visualization')
# plt.legend()
# plt.show()
