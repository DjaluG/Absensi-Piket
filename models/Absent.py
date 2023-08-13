from pydantic import BaseModel
from Student import Student

# Untuk yang tidak melaksanakan
class Absent(BaseModel):
    student: Student
    day: str
    date: str