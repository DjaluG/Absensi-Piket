from pydantic import BaseModel

# User untuk pengawas piket
class User(BaseModel):
    name: str
    password: str