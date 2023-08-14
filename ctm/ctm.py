from fastapi import APIRouter, UploadFile, File
import csv
from pymongo import MongoClient

app = APIRouter()


client = MongoClient('localhost', 27017)
db = client['absensi_piket']
collection = db['students']


#  CTM OR CSV TO MONGODB
@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    decoded_contents = contents.decode("utf-8")

    csv_reader = csv.DictReader(decoded_contents.splitlines())

    for row in csv_reader:

        collection.insert_one(row)

    return {"message": "Data CSV berhasil diimpor ke MongoDB"}


@app.on_event("shutdown")
def close_mongo_connection():
    client.close()
