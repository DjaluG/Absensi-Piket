from pydantic import BaseModel, validator
from models.User_role import UserRole

# class UserRole(str, Enum):
#     admin = "admin"
#     pengawas = "pengawas"

class User(BaseModel):
    name: str
    password: str
    role_id: int

# admin = User(name="admin", password="admin", role=UserRole.admin)

# responsible = User(
#     name="responsible", password="responsible", role=UserRole.pengawas)
