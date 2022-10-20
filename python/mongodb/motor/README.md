# MongoDB using Motor (Lib)

## Description

I have used async function as it is preferred.

## Requirements

```
pip install motor
```

## Use Case

### Intialize

```
DB_URL = "MongoDB URL"
DB_NAME = "MongoDB Name"
db = Database(DB_URL, DB_NAME)
```
### Assign & Accessing

- [Adding ID to the database](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L20)
  ```
  await db.add_id(id)
  ```

- [To check if id exists](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L24)
  ```
  await db.is_id_exist(id)
  ```
- [Get count of id in database](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L28)
  ```
  await db.total_count(id)
  ```
- [Get all id with info in the database](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L32)
  ```
  await db.get_all()
  ```
- [Delete particular id from database](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L36)
  ```
  await db.delete_by_id(id)
  ```
- [Set certain info of particular ID in database](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L39)
  ```
  await db.set_toDatabase(id, toDatabase)
  ```
- [Get certain info which we have saved of a particular ID](https://github.com/HeimanPictures/Databases/blob/0389ad80a1dbf494f1f1fc2d240f8b8eb26c4562/python/mongodb/motor/mongodb.py#L42)
  ```
  await db.get_toDatabase(id)
  ```

## Credits

- [**AkKiL**](https://github.com/HeimanPictures/)
