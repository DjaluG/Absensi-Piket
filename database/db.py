from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_db = f"""mongodb+srv://senaskot129:{password}@cluster0.juxx0tl.mongodb.net/"""
client = MongoClient(connection_db)
