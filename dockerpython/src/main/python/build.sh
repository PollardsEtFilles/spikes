#!/usr/bin/env bash

#pip install --trusted-host pypi -r requirements.txt
cp pypirc ~/.pypirc
python setup.py clean
python setup.py sdist upload -r internal
