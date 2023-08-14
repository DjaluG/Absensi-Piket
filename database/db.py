# from dotenv import load_dotenv, find_dotenv
# import os
# import pprint
from pymongo import MongoClient
# load_dotenv(find_dotenv())
# from motor.motor_asyncio import AsyncIOMotorClient

# url = "mongodb+srv://mongo:mongodb123@cluster0.cmqrijy.mongodb.net/piket_rayon?retryWrites=true&w=majority"
# url nya local dlu


def db_connection():
    url = "mongodb://localhost:27017/"
    db = MongoClient(url)
    return db['absensi_piket']

# password = os.environ.get("MONGODB_PWD")
# connection_db = f"""mongodb+srv://mongo:mongodb123@cluster0.cmqrijy.mongodb.net/piket_rayon?retryWrites=true&w=majority"""
# client = AsyncIOMotorClient(connection_db)

# dbs = client.list_database_names()
# test_db = client.test
# collection = test_db.list_collection_names()


# def insert_test_doc():
#     collection = test_db.test
#     test_documents = {
#         "name": "abisena",
#         "type": "tetst"
#     }
#     insert_id = collection.insert_one(test_documents).inserted_id
#     print(insert_id)


# insert_test_doc()
