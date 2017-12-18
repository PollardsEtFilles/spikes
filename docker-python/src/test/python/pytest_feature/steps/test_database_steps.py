
from pytest_bdd import scenario, given, when, then, parsers
import pytest
from pefspike.db import Database
from hamcrest import *
import subprocess
from subprocess import CalledProcessError


@pytest.fixture
def test_context():
    return dict()

@scenario('../database.feature', 'Import a database')
def test_create_a_database_connection():
    pass

# @given('a "employee" database on host "db" user "root" passwd "password"')
# def a_employee_database_on_host_db_user_root_passwd_password():
#     """a "employee" database on host "db" user "root" passwd "password"."""
#
#
# @when('we execute "src/test/resources/test_db-master/employees.sql"')
# def we_execute_srctestresourcestest_dbmasteremployeessql():
#     """we execute "src/test/resources/test_db-master/employees.sql"."""


# a "pefval_test" database on host "db" user "root" passwd "password"
@given(parsers.cfparse('a {database_name} database on host {host} user {user} passwd {passwd}'))
def context(database_name, host, user, passwd):
    context = test_context()
    context["my_database_name"] = database_name
    context["my_host"] = host
    context["my_user"] = user
    context["my_passwd"] = passwd
    return context

@when("a client connects")
def step_impl2(context):
    print(context)
    db = Database(context["my_host"], context["my_user"], context["my_passwd"], context["my_database_name"], 5)
    context["db"] = db
    db.connect()
    cur = db.connection.cursor(dictionary=True)
    pass

@when(parsers.cfparse('we execute {sql_file}'))
def import_file(context, sql_file):
    print(sql_file)
    context["db"].import_file(sql_file)
    pass

@when(parsers.cfparse('we import "{backup_file}"'))
def import_file(context, backup_file):
    context["db"].import_file(backup_file)
    pass

@when(parsers.cfparse('we import gzip "{backup_file}"'))
def import_gzip(context, backup_file):
    context["db"].import_gzip(backup_file)
    pass

@when(parsers.cfparse('the "{script_file}" database is imported from "{srcdir}" with "{options}"'))
def import_gzip(context, script_file, srcdir, options):
    try:
        # # cp .my.cnf to /root
        # out = subprocess.check_output('cp .my.cnf /root', shell=True, universal_newlines=True)
        # cd to import src dir first
        out = subprocess.check_output('cd '+srcdir+'; mysql --defaults-file='+options+' -h '+context['my_host']+'< '+script_file, shell=True, universal_newlines=True)
    except CalledProcessError:
        assert 0
    pass

@then(parsers.cfparse('there is some data in the "{table}" table'))
def step_impl(context, table):
    rows = context["db"].count(table)
    assert_that(rows, greater_than(100))
    pass

