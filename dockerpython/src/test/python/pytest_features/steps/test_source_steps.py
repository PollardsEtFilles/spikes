
from dockerpython.source import Source
from pytest_bdd import scenario, given, when, then
import pytest

# the fixture can have any name but must use the name for the parameter in all step functions
# otherwise dependency injection doesn't work
# the fixture contains data that is used in each step
@pytest.fixture
def state():
    return dict()

@scenario('../source.feature', 'Read a shell file into a Source class')
def test_publish():
    pass

# pytest magic ensures the fixture called state is provided to the test function
@given("a shell <file>")
def shellfile(state, file):
    state["file"] = file

@when("I read the file")
def loadfile(state):
    # this is only printed when an error occurs in the test
    print("afile", state["file"])
    state["source"] = Source(state["file"])

@then("Source.<prop> should equal <expected>")
def then_prop_equal_value(state, prop, expected):
    source = state["source"]
    actual = getattr(source, prop)
    assert actual == expected

