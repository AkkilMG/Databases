# AkKiL [github.com/HeimanPictures]

import json
from pymongo import MongoClient


class pyMongo:
  
    def __init__(self, host:str, port:int, db_name:str, table_name:str):
        try:
            myclient = pymongo.MongoClient(f"mongodb://{host}:{port}/")
            self.mydb = myclient[f"{db_name}"]
            self.mycollection = self.mydb[f"{table_name}"]
            self.auth = True
        except Exception:
            self.auth = False
        
    def insert(self, name:str, id:int, username:str, email:str):
        if (self.auth = True):
            try:
                record = {
                    NAME: name, 
                    ID: id,
                    USERNAME: username,
                    EMAIL: email
                } 
                rec = self.mydb.myTable.insert(record)
                return True
            except Exception:
                return False
        else:
            print("Please authenticate to move forward.")
            return False
        
    def find(self, value:json):
        if self.auth = True:
            try:
                fd = []
                for i in self.mydb.myTable.find(value):
                    fd.append(i)
                return True, fd
            except Exception:
                return False, None
        else:
            print("Please authenticate to move forward.")
            return False, None
    
    def count_all(self):
        if self.auth = True:
            try:
                count = self.mydb.myTable.find().count()
                return True, count
            except Exception:
                return False, 0
        else:
            print("Please authenticate to move forward.")
            return False, 0
    
    def count_of_value(self, value:json):
        if self.auth = True:
            try:
                count = self.mydb.myTable.find(value).count()
                return True, count
            except Exception:
                return False, 0
        else:
            print("Please authenticate to move forward.")
            return False, 0
                
    def get_all():
        if self.auth = True:
            try:
                all = []
                cursor = self.mycollection.find()
                for record in cursor:
                    all.append(record)
                return True, all
            except Exception:
                return False, None
        else:
            print("Please authenticate to move forward.")
            return False, None

    def update(self, many:bool, oldquery:json, newquery:json):
        if self.auth = True:
            try:
                if many == True:
                    self.mycollection.update_many(myquery, newquery)
                else:
                    self.mycollection.update_one(myquery, newquery)
                return True
            except Exception:
                return False
        else:
            print("Please authenticate to move forward.")
            return False
        
    def limit(self):
        if self.auth = True:
            try:
                lmt = []
                myresult = self.mycollection.find().limit(5)
                for i in myresult:
                    lmt.append(i)
                return True, lmt
            except Exception:
                return False, None
        else:
            print("Please authenticate to move forward.")
            return False, None

        
    def delete(self, myquery:json):
        if self.auth = True:
            try:
                mycol.delete_one(myquery)
                return True
            except Exception:
                return False
        else:
            print("Please authenticate to move forward.")
            return False
        
    def delete_all(self):
        if self.auth = True:
            try:
                mycol.delete_many({})
                return True
            except Exception:
                return False
        else:
            print("Please authenticate to move forward.")
            return False
        
    def delete_table(self):
        if self.auth = True:
            try:
                self.mycollection.drop()
                return True
            except Exception:
                return False
        else:
            print("Please authenticate to move forward.")
            return False
