from fastapi import APIRouter, HTTPException, Depends
from database.db import db_connection
from models.User import User, UserRole
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt
from auth.auth_data import get_users
auth_collection = db_connection()['auth']

app = APIRouter()


# @app.post('/login')
# async def login(user: User, user_role: UserRole):
#     query = [
#         {
#             "name": user.name,
#         }
#     ]
#     for item in query:
#         existing_user = auth_collection.find_one({"name": item["name"]})

#     if existing_user:
#         if existing_user["role"] == user_role.value:
#             return {"message": "Login successful"}
#         else:
#             raise HTTPException(status_code=403, detail="Invalid user role")
#     else:
#         raise HTTPException(
#             status_code=404, detail="User not found")

# Route Login menggunakan token
app.post('/login')
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
   user = get_users()
   users = None
   for us in user:
      if us.name == form_data.name:
          if bcrypt.checkpw(form_data.password.encode('utf-8'), us.password):
                users = us
                break
   if users is None:
       raise HTTPException(status_code=401, detail="Incorrect username or password")
   return {"access_token" : users['name'], "token_type" : "bearer"}