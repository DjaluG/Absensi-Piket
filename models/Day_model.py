from pydantic import BaseModel

class Day(BaseModel):
    id: int
    nama: str