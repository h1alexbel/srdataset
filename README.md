# srdataset

[![py](https://github.com/h1alexbel/srdataset/actions/workflows/make.yml/badge.svg)](https://github.com/h1alexbel/srdataset/actions/workflows/make.yml)
[![PDD status](http://www.0pdd.com/svg?name=h1alexbel/srdataset)](http://www.0pdd.com/p?name=h1alexbel/srdataset)
[![Hits-of-Code](https://hitsofcode.com/github/h1alexbel/srdataset)](https://hitsofcode.com/view/github/h1alexbel/srdataset)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/h1alexbel/srdataset/blob/master/LICENSE.txt)

SRdataset is an [unlabeled] dataset of GitHub repositories containing SRs
(sample repositories).

**Motivation**. During work on models for [samples-filter] project, we
discovered the need for the automation of the dataset building process
on remote servers, since we need to collect automatically a number of GitHub
repositories of data being productive in our research. In order to do this,
we integrated [ghminer] with a few scripts, and packaged all of that as Docker
container.

## How to use

To build a new version of dataset run this:

```bash
docker run --detach --name=srdataset --rm --volume "$(pwd):/srdataset" \
  -e "CSV=repos" \
  -e "SEARCH_QUERY=<query>" \
  -e "START_DATE=2019-01-01" \
  -e "END_DATE=2024-05-01" \
  -e "HF_TOKEN=xxx" \
  -e "INFERENCE_CHECKPOINT=sentence-transformers/all-MiniLM-L6-v2" \
  -e "PATS=pats.txt" \
  --oom-kill-disable \
  abialiauski/srdataset:0.0.1
```

Where `<query>` is the [search query] to the GitHub API,
`2019-01-01` is a start date to search the repositories those were created at
this date, `2024-05-01` is an end to search the repositories those were created
at this date, `xxx` is [HuggingFace token], required for accessing
[inference endpoint][HuggingFace Inference] in order to generate textual
embeddings; `pats.txt` is file contains a number of [GitHub PATs].

The building process can take a while. After it completed, you should have
these files:

* `results.csv` with all collected repositories.
* `repos.csv` with all preprocessed and filtered repositories.
* `texts.csv` repository textual metadata used for generating embeddings.
* `text-embeddings.csv` with ready-to-cluster repositories with textual vectors
only.
* `similar.csv` with input textual examples and their top-5 most similar
analogues from generated embeddings.
* `numerical.csv` with ready-to-cluster repositories with numerical data only.
* `mix.csv` with ready-to-cluster repositories that contain both: numerical and
textual vectors.

If you run container with `-e PUSH_TO_HF=true`, you should expect that after
preprocess, we will push output CSV files to the files to the profile, passed
to `-e HF_PROFILE`, within provided `HF_TOKEN`. All outputs will be pushed into
datasets with `sr-` prefix.

If you run container with `-e "CLUSTER=true"`, you should have one ZIP file
named like `clusters-2024-06-21-18:22.zip` and containing these files:

```text
agglomerative
  /mix
    /members
    ...
  /numerical
    /members
    ...
  /textual
    /members
    ...
dbscan/... (the same structure)
gmm/...
kmeans/...
source/...
```

All experiments are grouped by model name: `kmeans`, `dbscan`, `agglomerative`,
etc. In each that model directory you should have `members` directory and a set
of plots. `members` contains a set of text files tagged with output cluster
label e.g. `0.txt`. In `source` you should have all CSV files that were used to
generate clusters.

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full make build:

```bash
make env test
```

[unlabeled]: https://en.wikipedia.org/wiki/Unsupervised_learning
[samples-filter]: https://github.com/h1alexbel/samples-filter
[ghminer]: https://github.com/h1alexbel/ghminer
[GitHub PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[GitHub PATs]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[HuggingFace token]: https://huggingface.co/docs/hub/en/security-tokens
[HuggingFace Inference]: https://huggingface.co/inference-endpoints/dedicated
[search query]: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
