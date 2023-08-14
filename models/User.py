from pydantic import BaseModel
from enum import Enum


class UserRole(str, Enum):
    admin = "admin"
    pengawas = "pengawas"


class User(BaseModel):
    name: str
    password: str
    role: UserRole


admin = User(name="admin", password="admin", role=UserRole.admin)

responsible = User(
    name="responsible", password="responsible", role=UserRole.pengawas)
