#!/usr/bin/env bash

pip install --trusted-host pypi pefspike
pip install --trusted-host pypi pef.source
#python src/test/python/test_source.py
#behave src/test/python/features
pytest -vv --gherkin-terminal-reporter --junit-xml reports/pytest.xml src/test/python/pytest_feature


