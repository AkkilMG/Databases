# (c) AkKiL [github.com/HeimanPictures]

import mysql.connector


class MySQL():
    def __init__(self, user: str, passwd: str, database: str):
        self.user = user
        self.passwd = passwd
        self.database = database
        
    def new(self):
        self.dataBase = mysql.connector.connect(
          host = "localhost",
          user = self.user,
          passwd = self.passwd,
          database = self.database
        )
        
    def add_database(self):
        try:
            cursorObject = self.dataBase.cursor()
            cursorObject.execute(f"CREATE DATABASE {self.database}")
            self.dataBase.close()
            return True
        except Exception:
            return False
    
    def add_table(self):
        try:
            add_database()
            tableRecord = f"""CREATE TABLE {self.database} (
                               NAME  VARCHAR(20) NOT NULL,
                               ID INT NOT NULL,
                               USERNAME VARCHAR(15),
                               EMAIL VARCHAR NOT NULL
                               )"""
            cursorObject.execute(tableRecord)
            self.dataBase.close()
            return True
        except Exception:
            return False

    def insert(self, name:str, id:int, username:str, email:str):
        try:
            sql = f"INSERT INTO {self.database} (NAME, ID, USERNAME, EMAIL)\
            VALUES (%s, %d, %s, %s)"
            val = (name, id, username, email)
            cursorObject.execute(sql, val)
            self.dataBase.commit()
            self.dataBase.close()
            return True
        except Exception:
            return False

    def fetch_condition(self, condition:bool):
        try:
            if condition == True:
                query = f"SELECT NAME, ID, EMAIL FROM {self.database}"
            else:
                query = f"SELECT * FROM {self.database} where ID >=202200"
            cursorObject.execute(query)
            myresult = cursorObject.fetchall()
            self.dataBase.close()
            return True
        except Exception:
            return False
        
    def fetch_order(self):
        try:
            query = f"SELECT * FROM {self.database} ORDER BY NAME DESC"
            cursorObject.execute(query)
            myresult = cursorObject.fetchall()
            self.dataBase.close()
            return True, myresult
        except Exception:
            return False, None
                
    def fetch_limit(self):
        try:
            query = f"SELECT * FROM {self.database} LIMIT 2 OFFSET 1"
            cursorObject.execute(query)
            myresult = cursorObject.fetchall()
            self.dataBase.close()
            return True
        except Exception:
            return False
        
    def update(self, email:str, new_username:str):
        try:
            query = f"UPDATE {self.database} SET USERNAME = {new_username} WHERE EMAIL ='{email}'"
            cursorObject.execute(query)
            self.dataBase.commit()
            self.dataBase.close()
            return True
        except Exception:
            return False
        
    def delete_username_list_table(self, username:str):
        try:
            query = f"DELETE FROM {self.database} WHERE USERNAME = '{username}'"
            cursorObject.execute(query)
            self.dataBase.commit()
            self.dataBase.close()
            return True
        except Exception:
            return False
        
    def delete_table(self, condition:bool):
        try:
            if condition == True:
                query = f"Drop Table if exists USERNAME;"
            else:
                query = f"DROP TABLE {self.database};"
            cursorObject.execute(query)
            self.dataBase.commit()
            self.dataBase.close()
            return True
        except Exception:
            return False
        
