from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False
    context.previousStep = False

@then('behave will test it for us')
def step_impl(context):
    print('context:', context)
    assert context.previousStep is False