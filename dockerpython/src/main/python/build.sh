#!/usr/bin/env bash

# need pypirc to write to the local pypi server
# reading doesn't need this just the PIP_EXTRA_INDEX_URL environment variable
# e.g. PIP_EXTRA_INDEX_URL=http://pypi:80/simple/
cp pypirc ~/.pypirc
python setup.py clean
python setup.py sdist upload -r internal
