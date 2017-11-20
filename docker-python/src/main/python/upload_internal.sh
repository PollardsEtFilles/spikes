#!/usr/bin/env bash

cp pypirc ~/.pypirc
python setup.py clean
python setup.py sdist upload -r internal
