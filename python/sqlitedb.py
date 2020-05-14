import sqlite3
import os
import pathlib



cwd = os.getcwd()


class Base_db:

    def __init__(self, dbname, tablelist=None, tablesdict=None):
        dbFolder = 'python/SQLite'
        self.dbname = dbname
        if tablelist is None:
            self.tablelist = []
        else:
            self.tablelist = tablelist

        if tablesdict is None:
            self.tablesdict = {}
        else:
            self.tablesdict = tablesdict


    def createtable(self, tname, tcollumns):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        statement = 'CREATE TABLE {} ({})'.format(tname, tcollumns)
        c.execute(statement)
        conn.commit()
        conn.close()
        self.tablelist.append(tname)


    def insert(self, tname,cvalue,cdata):
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()
        statement = "'INSERT INTO {} Values ({})', {}".format(tname, cvalue, cdata)
        c.execute(statement)
        conn.commit()
        conn.close()

