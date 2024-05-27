# srdataset

[![py](https://github.com/h1alexbel/srdataset/actions/workflows/make.yml/badge.svg)](https://github.com/h1alexbel/srdataset/actions/workflows/make.yml)
[![PDD status](http://www.0pdd.com/svg?name=h1alexbel/srdataset)](http://www.0pdd.com/p?name=h1alexbel/srdataset)
[![Hits-of-Code](https://hitsofcode.com/github/h1alexbel/srdataset)](https://hitsofcode.com/view/github/h1alexbel/srdataset)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/h1alexbel/srdataset/blob/master/LICENSE.txt)

SRdataset is an [unlabeled] dataset of GitHub repositories containing SRs
(sample repositories).

**Motivation**. During work on models for [samples-filter] project, we
discovered the need for the automation of the dataset building process
on remote servers, since we need to collect big amount of data being productive
in our research. In order to do this, we integrated [ghminer] with a few
infrastructure scripts, and packaged all of that into Docker container.

## How to use

To build a new version of dataset run this:

```bash
docker run --detach --name=srdataset --rm --volume "$(pwd):/srdataset" \
  -e "GITHUB_TOKEN=XXX" \
  -e "DESTINATION=h1alexbel/samples-filter" \
  -e "DESTINATION_BRANCH=dataset" \
  -e "SEARCH_QUERY=<query>" \
  -e "START_DATE=2019-01-01" \
  -e "END_DATE=2024-05-01" \
  -e "PATS=pats.txt" \
  --oom-kill-disable \
  abialiauski/srdataset:0.0.1
```

Where `XXX` is a [GitHub PAT] with WRITE permissions to
`h1alexbel/samples-filter`, `dataset` branch, which is place, where all output
files will be delivered, `<query>` is the [search query] to the GitHub API,
`2019-01-01` is a start date to search the repositories those were created at
this date, `2024-05-01` is an end to search the repositories those were created
at this date, `pats.txt` is file contains a number of [GitHub PATs].

The building process can take a while. After it completed, you should have
`dataset.csv` file with all collected repositories. If you included
`GITHUB_TOKEN`, it should be pushed to `DESTINATION` right into
`DESTINATION_BRANCH`.

## How it works

TBD..

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full make build:

```bash
make lint test
```

[unlabeled]: https://en.wikipedia.org/wiki/Unsupervised_learning
[samples-filter]: https://github.com/h1alexbel/samples-filter
[ghminer]: https://github.com/h1alexbel/ghminer
[GitHub PAT]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[GitHub PATs]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[search query]: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories
