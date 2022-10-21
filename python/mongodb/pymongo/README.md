# MongoDB using pymongo

## Description

> This is basic code for pymongo for mongodb which is one of the most used database in recent days.

## Requirements

```
pip install pymongo
```

## Use Case

### Intialize

```
host = "localhost"
port = 27017
db_name = "database name"
table_name = "A Table name for the database"
mongo = pyMongo(host, port, db_name, table_name)
```

### Assign & Accessing

- [Insert to the table created](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L18)
  ```
  name = "Akkil"
  id = 202200
  username = "HeimanPictures"
  email = "example@domain.com"
  a = mongo.insert(name, id, username, email) # a -> returns boolean
  ```
- [Find a particular value](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L35)
  ```
  array = []
  a, array = mongo.find_id({ID: 202200}) # a -> returns boolean, array -> array of values/None
  ```
- [Count all in the table](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L48)
  ```
  a, count = mongo.count_all() # a -> returns boolean, count -> gives count/0
  ```
- [Count number of result which has particular value](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L59)
  ```
  mongo.count_of_name("Akkil") # a -> returns boolean, count -> gives count/0
  ```
- [Get all values in the database](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L70)
  ```
  array = []
  a, array = mongo.get_all() # a -> returns boolean, array -> array of values/None
  ```
- [Updates certain values in the database (For example: Email in this case)](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L84)
  ```
  many = False
  oldquery = "example@domain.com"
  newquery = "example@domain.io"
  a = mongo.update_email(many, oldquery, newquery) # a -> returns boolean
  ```
- [Get Limited values as per choice](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L98)
  ```
  array = []
  limt = 5
  a, array = mongo.limit(limt) # a -> returns boolean, array -> array of values/None
  ```
- [Delete values of particular ID](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L113)
  ```
  a = mongo.delete_id(202200) # a -> returns boolean
  ```
- [Delete all values in table](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L124)
  ```
  a = delete_all() # a -> returns boolean
  ```
- [Delete whole table](https://github.com/HeimanPictures/Databases/blob/6a8e18cefc5136d13b3f33a1bd78ae624ad33584/python/mongodb/pymongo/pymongo.py#L135)
  ```
  a = delete_table() # a -> returns boolean
  ```

## Credits

- [**AkKiL**](https://github.com/HeimanPictures/)
