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

FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-eo", "pipefail", "-c"]

# Build essentials that are required later
RUN apt-get update -y --fix-missing
RUN apt-get install -y --no-install-recommends make=4.3-4.1build2
RUN apt-get install -y --no-install-recommends git
RUN apt-get install -y --no-install-recommends npm
RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends python3-venv

# Setup Python venv.
WORKDIR /srdataset
COPY requirements.txt /srdataset/
RUN python3 -m venv .venv && /srdataset/.venv/bin/python -m pip install -r requirements.txt
ENV PYTHON=/srdataset/.venv/bin/python

COPY Makefile /srdataset/
ENV LOCAL /srdataset
COPY steps/install.sh /srdataset/steps/
RUN sh steps/install.sh
COPY . /srdataset
ENTRYPOINT make collect formalize
