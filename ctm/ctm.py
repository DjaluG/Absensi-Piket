from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import csv
from pymongo import MongoClient
from auth.auth_handler import get_current_user
from models.User import User

app = APIRouter()


client = MongoClient('localhost', 27017)
db = client['absensi_piket']
collection = db['students']


#  CTM OR CSV TO MONGODB
@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    if current_user.role_id != 1:
        raise HTTPException(status_code=403, detail="Forbidden")

    contents = await file.read()
    decoded_contents = contents.decode("utf-8")

    csv_reader = csv.DictReader(decoded_contents.splitlines())

    for row in csv_reader:

        collection.insert_one(row)

    return {"message": "Data CSV berhasil diimpor ke MongoDB"}


@app.on_event("shutdown")
def close_mongo_connection():
    client.close()
