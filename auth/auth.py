from fastapi import APIRouter, HTTPException
from database.db import db_connection
from models.User import User, UserRole
auth_collection = db_connection()['auth']

app = APIRouter()


@app.post('/login')
async def login(user: User, user_role: UserRole):
    query = [
        {
            "name": user.name,
        }
    ]
    for item in query:
        existing_user = auth_collection.find_one({"name": item["name"]})

    if existing_user:
        if existing_user["role"] == user_role.value:
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=403, detail="Invalid user role")
    else:
        raise HTTPException(
            status_code=401, detail="Invalid username or password")
