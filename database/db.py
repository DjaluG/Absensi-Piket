from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_db = f"""mongodb+srv://mongo:{password}@cluster0.cmqrijy.mongodb.net/?retryWrites=true&w=majority"""
client = MongoClient(connection_db)

dbs = client.list_database_names()
test_db = client.test
collection = test_db.list_collection_names()


def insert_test_doc():
    collection = test_db.test
    test_documents = {
        "name": "abisena",
        "type": "tetst"
    }
    insert_id = collection.insert_one(test_documents).inserted_id
    print(insert_id)


insert_test_doc()
