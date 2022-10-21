# MySQL

## Description

We use MySQL in python by using library like mysql-connector-python which allows the conversion between Python and MySQL data types.

## Requirements

```
pip3 install mysql-connector-python
```

## Use Case

### Intialize

```
user = "user"
passwd = "password"
database = "db"
mysql = MySQL(user, passwd, database)
mysql.add_table()
```

### Assign & Accessing

All the returns boolean value

- [Insert data into database](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L44)
  ```
  name = "Akkil"
  id = 202200
  username = "HeimanPictures"
  email = "example@domain.com"
  a = mysql.insert(name, id, username, email) # a -> returns boolean
  ```
- [Fetching details with condtion or not (For example: with comparison operators)](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L56)
  ```
  condition = True
  mysql.fetch_condition(condition) # a -> returns boolean
  ```
- [Fetch in order (For example: here its in order of name with DESC-Describe)](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L69)
  ```
  a = mysql.fetch_order() # a -> returns boolean
  ```
- [Fetch with limit](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L79)
  ```
  a = mysql.fetch_limit() # a -> returns boolean
  ```
- [Update a particular value using certain other constant value](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L89)
  ```
  email = "example@domain.com"
  username = "TheAkkil"
  a = mysql.update(email, username) # a -> returns boolean
  ```
- [Delete a particular values of certain username in this reference](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L99)
  ```
  username = "TheAkkil"
  a = mysql.delete_username_list_table(username) # a -> returns boolean
  ```
- [Delete whole table with certain condition or not](https://github.com/HeimanPictures/Databases/blob/525f7fe61c55511559afef131ebac17c53853c55/python/mysql/mysql.py#L109)
  ```
  condition = False
  a = mysql.delete_table(condition) # a -> returns boolean
  ```
  
## Credits

- [**AkKiL**](https://github.com/HeimanPictures/)
