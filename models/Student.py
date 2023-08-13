from pydantic import BaseModel

class Student(BaseModel):
    nis: str
    nama: str
    rombel: str
    rayon: str