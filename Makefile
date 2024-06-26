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

.SHELLFLAGS: -e -o pipefail -c
.ONESHELL:
.PHONY: env install collect metrics test
.SILENT:

## The shell to use.
SHELL := bash

# Setup environment.
env:
	python3 -m pip install --upgrade pip
	pip3 install -r requirements.txt
	pip3 install .

# Test.
test:
	export PYTHONPATH=.
	python3 -m pytest tests

# Cluster.
cluster:
	chmod +x steps/cluster.sh &&./steps/cluster.sh
	chmod +x steps/zip.sh &&./steps/zip.sh

# Install.
install:
	chmod +x steps/install.sh &&./steps/install.sh

# Collect repositories from GitHub API.
collect:
	chmod +x steps/collect.sh &&./steps/collect.sh

# Formalize and prepare collected dataset.
formalize:
	chmod +x steps/formalize.sh &&./steps/formalize.sh
