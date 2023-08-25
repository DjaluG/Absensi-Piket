from pydantic import BaseModel
from typing import Optional

# Model Siswa
class Student(BaseModel):
    nis: str
    nama: str
    rombel: str
    day: str
    date: Optional[str]
    status: str
    total: Optional[str]