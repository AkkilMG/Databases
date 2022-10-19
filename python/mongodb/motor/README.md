# MongoDB using Motor (Lib)

## Description

I have used async function as it is preferred.

## Use Case

### Intialize

```
DB_URL = "MongoDB URL"
DB_NAME = "MongoDB Name"
db = Database(DB_URL, DB_NAME)
```
### Assign & Accessing

- Adding ID to the database
  ```
  await db.add_user(id)
  ```

- To check if id exists
  ```
  await db.is_id_exist(id)
  ```
- Get count of id in database
  ```
  await db.total_count(id)
  ```
- Get all id with info in the database
  ```
  await db.get_all()
  ```
- Delete particular id from database
  ```
  await db.delete_by_id(id)
  ```
- Set certain info of particular ID in database
  ```
  await db.set_toDatabase(id, toDatabase)
  ```
- Get certain info which we have saved of a particular ID
  ```
  await db.get_toDatabase(id)
  ```

## Credits

- [AkKiL](https://github.com/HeimanPictures/)
