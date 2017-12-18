# PEF Docker Python Experimental Spike

## Purpose and Description
The purpose of this project is to demonstrate how to:
* use Docker for writing and testing Python code
* create Python modules with appropriate package naming conventions
* upload a Python module to a pypi server
* write BDD tests using Python Behave
* write BDD tests using Python pytest
* run tests in a docker container using gradle
* run tests in docker compose
* visualise the test results in Intellij's Idea's test runner

As a side benefit it allows PEF to evaluate which BDD framework is appropriate for their tests.

PEF are a major user of Python in their processing pipelines. Its proving to be quick and easy to develop 
applications with Python without a lot of the baggage associated with industrial languages like Java or C++.
Its primary use has been in ETL type of applications but PEF also intend to use it for financial analytic 
applications.

The project contains a single module called pef.source which performs a similar function to bash source, that is
it creates a Python class containing attributes that map to environment variables in the shell script. This allows
PEF to "source" shell scripts in Python applications like bash. For instance,
```$python
asource = Source('src/test/env/env.sh')
print(asource.variable)
```
This project contains two sets of code following Java directory conventions that is 
* src/main/python for application code
* src/test/python for test code and features


## Download Database Import File
cd docker-python
curl https://codeload.github.com/datacharmer/test_db/zip/master -o master.zip
unzip master.zip


## Running Python Tests
First build the required images, these are:
* ../docker/pypiserver/build.sh
* ../docker/python3/build.sh

Then run tests as follows:

| Command | Purpose |
| ------- | ------- |
../gradlew behave  | Run behave tests in a docker container. This test does not deploy a python package.
../gradlew pytest  | Run pytest tests in a docker container. This test does not deploy a python package.
../gradlew testall | Run both pytest and behave above
../gradlew test    | Run all tests and both pytest and behave above. This is standard Gradle.
docker-compose run main   | Build the Python module pef.source in src/main/python and deploy to a local pypi server.
docker-compose run test   | Test the Python module pef.source downloaded from local pypi server with behave and pytest.
docker-compose run behave | Run behave tests in a docker container. This test does not deploy a python package.
docker-compose run pytest | Run pytest tests in a docker container. This test does not deploy a python package.


## Discussion
The gradle scripts are configured to output junit style xml as well as human readable text output.
However, its not possible to display the test results in the Intellij IDEA's test runner.
Debugging Python is also more difficult when running in a container. However, the advantages of
not using virtual environments outweight this limitation especially if a good set of tests are
written.

## Testing Framework in PEF
We choose behave because:
* the output is more readable
* there is less magic with fixtures

but don't like:
* steps have to be next to fixtures so its less flexible

## References
https://docs.pytest.org/en/latest/index.html
https://docs.pytest.org/en/latest/contents.html#toc
https://docs.pytest.org/en/latest/fixture.html#fixture
https://pypi.python.org/pypi/pytest-bdd
https://pythonhosted.org/behave/index.html
https://pythonhosted.org/behave/tutorial.html
https://pypi.python.org/pypi/behave-pytest/0.1.1
https://github.com/ribozz/behave-pytest
