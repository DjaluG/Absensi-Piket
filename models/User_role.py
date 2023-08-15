from pydantic import BaseModel

class UserRole(BaseModel):
    # Gunakan Integer supaya mudah untuk dipanggil di model User
    id: int
    title : str
