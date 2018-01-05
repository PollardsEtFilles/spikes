#!/usr/bin/env bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pip install --trusted-host pypi -r ${script_dir}/requirements-test.txt

pytest ${script_dir}/unit -v
#behave --junit ${script_dir}/features
#pytest -v --gherkin-terminal-reporter -vv --junit-xml reports/pytest.xml ${script_dir}/pytest_features


