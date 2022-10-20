# (c) AkKiL [github.com/HeimanPictures]

import mysql.connector


class MySQL():
    def __init__(self, user: str, passwd: str, database: str):
        self.user = user
        self.passwd = passwd
        self.database = database
        
    def new(self):
        dataBase = mysql.connector.connect(
          host ="localhost",
          user =self.user,
          passwd =self.passwd,
          database =self.database
        )
        
    def add_database(self):
        cursorObject = dataBase.cursor()
        cursorObject.execute(f"CREATE DATABASE {self.database}")
        return True
    
    def add_table(self):
        add_database()
        
        # creating table
        tableRecord = """CREATE TABLE db (
                           NAME  VARCHAR(20) NOT NULL
                           )"""
