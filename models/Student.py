from pydantic import BaseModel

# Model Siswa
class Student(BaseModel):
    nis: str
    nama: str
    rombel: str
    rayon: str