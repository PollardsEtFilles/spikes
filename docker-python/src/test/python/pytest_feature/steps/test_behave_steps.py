
from source import Source
from pytest_bdd import scenario, given, when, then
import pytest

@pytest.fixture
def test_state():
    return dict()

@scenario('../behave.feature', 'run a simple test')
def test_behave():
    pass

# pytest magic ensures the fixture called state is provided to the test function
@given("we have behave installed")
def test_given_behave(test_state):
    print("given")

@when("we implement a test")
def test_when_behave(test_state):
    print("when")

@then("behave will test it for us")
def test_then_behave(test_state):
    print("then")

