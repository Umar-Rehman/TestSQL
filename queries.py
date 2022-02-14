import pyodbc
import pandas as pd
import csv

class SQLQuery():
    def __init__(self, driver, server, db_name = None, table_name = None):
        self.driver = driver
        self.server = server
        self.db_name = db_name
        self.table_name = table_name

    def execute_query(self, sqlStr):
        conn = pyodbc.connect("driver={%s};server=%s;database=master;trusted_connection=true" % (self.driver, self.server),autocommit=True)
        cur = conn.cursor()
        try:
            cur.execute(sqlStr)
        except Exception as e:
            outcome_msg = f"Query failed: {str(e)}"
            print(outcome_msg)
            return outcome_msg
        conn.close()
        outcome_msg = f"Query succeeded."
        print(outcome_msg)
        return outcome_msg

    def create_db(self):
        """Creates a new database in SQL Server instance"""
        db_name=input("Enter name of new database: ")
        sqlStr = f"CREATE DATABASE {db_name}"

        self.execute_query(sqlStr)

    def drop_db(self):
        """Drops an existing database in SQL Server instance"""

        db_name=input("Enter name of database to drop: ")
        sqlStr = f"DROP DATABASE IF EXISTS {db_name}"

        self.execute_query(sqlStr)

    def get_tables(self):
        tables = []
        if self.db_name == None:
            self.db_name = input("Enter name of database to view tables: ")
        conn = pyodbc.connect("driver={%s};server=%s;database=%s;trusted_connection=true" % (self.driver, self.server, self.db_name),autocommit=True)
        cur = conn.cursor()
        sqlStr = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"
        cur.execute(sqlStr)
        for i in cur:
            tables.append(i[0])
        conn.close()
        return tables

    def get_columns(self):
        columns =[]
        if self.db_name == None:
            self.db_name = input("Enter name of database: ")
        if self.table_name == None:
            self.table_name = input("Enter table name: ")
        conn = pyodbc.connect("driver={%s};server=%s;database=%s;trusted_connection=true" % (self.driver, self.server, self.db_name),autocommit=True)
        cur = conn.cursor()
        sqlStr = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{self.table_name}'"
        cur.execute(sqlStr)
        for i in cur:
            columns.append(i[0])
        conn.close()
        return columns

    def insert_data_from_csv(self, csv_file):
        if self.db_name == None:
            self.db_name = input("Enter name of database: ")
        conn = pyodbc.connect("driver={%s};server=%s;database=%s;trusted_connection=true" % (self.driver, self.server, self.db_name),autocommit=True)
        cur = conn.cursor()
        if self.table_name == None:
            self.table_name = input("Enter table name to insert data into: ")
        with open (csv_file, 'r') as f:
            reader = csv.reader(f)
            columns = next(reader)
            table_columns = SQL.get_columns()
            if len(columns) == len(table_columns):
                query = 'insert into {0}({1}) values ({2})'
                query = query.format(self.table_name, ','.join(columns), ','.join('?' * len(columns)))
                for data in reader:
                    cur.execute(query, data)
                conn.close()
            else:
                print("Number of columns in of SQL Table does not match number of columns in selected csv file.")
                pass


# SQL = SQLQuery("SQL Server", ".\SQLExpress", "Lab8", "Student")
# SQL.get_tables()
# SQL.get_columns()
# SQL.insert_data_from_csv()


# with open('students.csv') as csv_file:

#     list_of_column_names = []
#     csv_reader = csv.reader(csv_file, delimiter = ',')

#     for row in csv_reader:
#         list_of_column_names.append(row)
#         break
    
#     list_of_column_names = list_of_column_names[0]

# driver = "SQL Server"
# server = ".\SQLExpress"
