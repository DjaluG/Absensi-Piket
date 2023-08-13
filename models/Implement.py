from pydantic import BaseModel
from Student import Student

# Untuk yang melaksanakan piket
class Implement(BaseModel):
    student: Student
    day: str
    date: str
    time: str