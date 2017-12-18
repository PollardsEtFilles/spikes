from behave import *
import mysql.connector,getpass, smtplib, time
from mysql.connector import errorcode
from pefspike.db import Database
from hamcrest import *
import subprocess
from subprocess import CalledProcessError

#use_step_matcher("re")


# a "pefval_test" database on host "db" user "root" passwd "password"
@given(u'a "{database_name}" database on host "{host}" user "{user}" passwd "{passwd}"')
def step_impl1(context, database_name, host, user, passwd):
    context.my_database_name = database_name
    context.my_host = host
    context.my_user = user
    context.my_passwd = passwd
    pass

@when("a client connects")
def step_impl2(context):
    context.db = Database(context.my_host, context.my_user, context.my_passwd, context.my_database_name, 5)
    context.db.connect()
    cur = context.db.connection.cursor(dictionary=True)
    pass

@when('the "{script_file}" database is imported from "{srcdir}" with "{options}"')
def import_gzip(context, script_file, srcdir, options):
    try:
        # # cp .my.cnf to /root
        # out = subprocess.check_output('cp .my.cnf /root', shell=True, universal_newlines=True)
        # cd to import src dir first
        out = subprocess.check_output('cd '+srcdir+'; mysql --defaults-file='+options+' -h '+context.my_host+'< '+script_file, shell=True, universal_newlines=True)
    except CalledProcessError:
        assert 0
    pass

@when('we import "{backup_file}"')
def import_file(context, backup_file):
    context.db.drop()
    context.db.create()
    context.db.import_file(backup_file)
    pass

@when('we import gzip "{backup_file}"')
def import_gzip(context, backup_file):
    context.db.drop()
    context.db.create()
    context.db.import_gzip(backup_file)
    pass

@then('there is some data in the "{table}" table')
def step_impl(context, table):
    rows = context.db.count(table)
    assert_that(rows, greater_than(100))
    pass

