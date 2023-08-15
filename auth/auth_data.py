import bcrypt
from models.User import User

def get_users():
    users = [
        User(name='admin', password= bcrypt.hashpw(b'admin', bcrypt.gensalt()), role= 1),
        User(name='responsible', password= bcrypt.hashpw(b'responsible', bcrypt.gensalt()), role= 2),
    ]
    return users
