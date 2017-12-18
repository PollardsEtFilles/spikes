
from pefspike.source import Source
from behave import *


@given("a shell {file}")
def sshellfile(context, file):
    print("afile1", file)
    context.file = file

@when("I read the file")
def sloadfile(context):
    print("afile1", context.file)
    # this is only printed when an error occurs in the test
    # print("afile2", context.file)
    context.source = Source(context.file)

@then("Source.{prop} should equal {expected}")
def sthen_prop_equal_value(context, prop, expected):
    print("afile1", context.file)
    source = context.source
    actual = getattr(source, prop)
    assert actual == expected

