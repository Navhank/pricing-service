import pymongo
import os

class Database:
    URI = os.environ.get("MONGODB_URI", None)
    DATABASE = pymongo.MongoClient(URI).get_database()

    @staticmethod
    def insert(collection: str, data: dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict) -> dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: dict, data:dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: dict) -> dict:
        return Database.DATABASE[collection].remove(query)
