import mysql.connector
import time
from mysql.connector import errorcode
import gzip


class Database():

    def __init__(self, host, user, passwd, db, tries):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.tries = tries

    def connect(self):
        connecting = True
        tries = 0

        print("connecting", self.host, self.user, self.passwd, self.db)
        while connecting:
            try:
                print("tries=", tries)
                time.sleep(1)
                self.connection = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd) #, db=self.db)
                connecting = False
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exists")
                else:
                    print(err)
                if tries > self.tries:
                    connecting = False
                else:
                    tries = tries + 1
            else:
                return self.connection

    def connection(self):
        return self.connection

    def drop(self):
        query = "drop database if exists `%s`;" % self.db
        self.connection.cursor(dictionary=True).execute(query)

    def create(self):
        query = "create database if not exists `%s`;" % self.db
        self.connection.cursor(dictionary=True).execute(query)

    def import_file(self, backup_file):
        with open(backup_file, 'r') as f:
            sql = f.read()
        self.executeScripts(sql)

    def import_gzip(self, backup_file):
        with gzip.open(backup_file, 'rt') as f:
            sql = f.read()
        print(sql)
        self.executeScripts(sql)

    def count(self, table):
        self.connection.database = self.db
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("select count(*) as cnt from `%s`" % table)
        row = cursor.fetchone()
        return row['cnt']

    def executeScript(self, sql):
        try:
            cursor = self.connection.cursor(dictionary=True, buffered=True)
            self.connection.database = self.db
            cursor.execute(sql)
        except mysql.connector.Error as err:
            print("Command skipped: ", err)
        self.connection.commit()

    def executeScripts(self, sql):
        cursor = self.connection.cursor(dictionary=True, buffered=True)
        self.connection.database = self.db
        sqlCommands = sql.split(';')

        for command in sqlCommands:
            try:
                if command.strip() != '':
                    cursor.execute(command)
            except mysql.connector.Error as err:
                print("Command skipped: ", err)
        self.connection.commit()
