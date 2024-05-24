# Sample GitHub repositories dataset (SRdataset)

## How to use

TBD..

## How to build

To build a new version of dataset run this either on cloud VM or locally:

```bash
docker run --detach --name=dataset --rm --volume "$(pwd):/dataset" \
  -e "GITHUB_TOKEN=XXX" \
  -e "DESTINATION=h1alexbel/samples-filter" \
  -e "DESTINATION_BRANCH=dataset" \
  -e "SEARCH_QUERY=<query>" \
  -e "START_DATE=2019-01-01" \
  -e "END_DATE=2024-05-01" \
  -e "PATS=pats.txt" \
  --oom-kill-disable \
  h1alexbel/srdataset:0.0.1 "make -e >/dataset/make.log 2>&1"
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

## How to contribute

Fork repository, make changes, send us a [pull request](https://www.yegor256.com/2014/04/15/github-guidelines.html).
We will review your changes and apply them to the `master` branch shortly,
provided they don't violate our quality standards. To avoid frustration,
before sending us your pull request please run full make build:

```bash
make lint test
```
