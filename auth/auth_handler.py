# auth_handler.py
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Depends
from auth.auth_data import get_users
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# sebagai middleware 
def get_current_user(token: str = Depends(oauth2_scheme)):
    users = get_users()
    user = None
    for us in users:
        if bcrypt.checkpw(us.name.encode('utf-8'), token.encode('utf-8')):
            user = us
            break
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user
