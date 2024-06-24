import pandas as pd
from sklearn.mixture import GaussianMixture

from steps.members_to_txt import to_txt

frame = pd.read_csv("numerics.csv")
gmm = GaussianMixture(n_components=6, random_state=1)
frame["cluster"] = gmm.fit_predict(
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
to_txt(clusters, "clusters/gmm/numerical/members")
