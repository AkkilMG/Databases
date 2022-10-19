# (c) AkKiL [github.com/HeimanPictures]


import datetime
import motor.motor_asyncio


class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_id(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat()
        )

    async def add_id(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_id_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return True if user else False

    async def total_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all(self):
        all_users = self.col.find({})
        return all_users

    async def delete_by_id(self, id):
        await self.col.delete_many({"id": int(id)})

    async def set_toDatabase(self, id, toDatabase):
        await self.col.update_one({"id": id}, {"$set": {"toDatabase": toDatabase}})

    async def get_toDatabase(self, id):
        user = await self.col.find_one({"id": int(id)})
        return user.get("toDatabase", None)

