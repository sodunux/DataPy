import pymysql as ms
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class mysqlpy:
    def __init__(self):
        self.connect()
        pass

    def connect(self):
        self.db = ms.connect('localhost', 'root', '', 'TESTDB')
        self.cursor = self.db.cursor()
        self.cursor.execute('SELECT VERSION()')
        dat = self.cursor.fetchone()

    def close(self):
        self.db.close()

    def create_table(self):
        sql = "DROP TABLE IF EXISTS EMPLOYEE"
        self.cursor.execute(sql)
        sql = """CREATE TABLE EMPLOYEE (
         	FIRST_NAME  CHAR(20) NOT NULL,
         	LAST_NAME  CHAR(20),
         	AGE INT,  
         	SEX CHAR(1),
         	INCOME FLOAT )"""
        self.cursor.execute(sql)

    def insert_table(self):
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         	LAST_NAME, AGE, SEX, INCOME)
         	VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        self.cursor.execute(sql)
        self.db.commit()

    def __del__(self):
        self.close()


if __name__ == '__main__':
    dms = mysqlpy()
    dms.insert_table()
