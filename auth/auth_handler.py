# auth_handler.py
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from database.db import db_connection
from auth.auth_data import get_users
import bcrypt

auth_collection = db_connection()['auth']
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# sebagai middleware 
def get_current_user(token: str = Depends(oauth2_scheme)):
    users = get_users()
    # users = get_users()
    user = next((us for us in users if us.name == token), None)
        
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
        
    return user
