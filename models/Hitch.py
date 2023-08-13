from pydantic import BaseModel
from Student import Student

# Untuk yang berhalang sakit, izin, Alpha
class Hitch(BaseModel):
    student: Student
    day: str
    date: str
    reason: str