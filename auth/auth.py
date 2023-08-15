from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database.db import db_connection
from models.User import User, UserRole
import bcrypt

auth_collection = db_connection()['auth']

app = APIRouter()


@app.post('/login')
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    existing_user = auth_collection.find_one({"name": form_data.username})

    if existing_user:
        if bcrypt.checkpw(form_data.password.encode('utf-8'), existing_user["password"]):
            return {"access_token": existing_user['name'], "token_type": "bearer"}
        else:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password")
    else:
        raise HTTPException(status_code=404, detail="User not found")
