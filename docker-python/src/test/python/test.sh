#!/usr/bin/env bash

pip install --trusted-host pypi source
python test_source.py
behave
pytest
