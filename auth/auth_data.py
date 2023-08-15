import bcrypt
from models.User import User


def get_users():
    users = [
        User(name='admin', password=bcrypt.hashpw(
            b'admin', bcrypt.gensalt()), role_id=1),
        User(name='responsible', password=bcrypt.hashpw(
            b'responsible', bcrypt.gensalt()), role_id=2),
    ]
    return users
