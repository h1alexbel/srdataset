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

frame = pd.read_csv('results.csv')
frame["ic"] = frame["issues"] / frame["commits"]
# @todo #7:30min Compute CPD and RC metrics too.
#  We need to compute CPD and RC metrics too, however for now we don't have
#  the proper dataset after ghminer execution. Need to collect required data
#  first, and then compute CPDs and RCs. Don't forget to remove this puzzle.
frame.drop(
    columns=[
        "branch",
        "createdAt",
        "lastCommitDate",
        "lastReleaseDate",
        "contributors",
        "pulls",
        "commits",
        "issues",
        "forks",
        "stars",
        "license",
        "language",
        "diskUsage"
    ],
    inplace=True
)
frame.to_csv("repos.csv", index=False)
