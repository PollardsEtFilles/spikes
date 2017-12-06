#!/usr/bin/env bash

pip install --trusted-host pypi pef.source
python src/test/python/test_source.py
behave src/test/python/features
pytest src/test/python
