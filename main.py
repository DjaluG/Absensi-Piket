from fastapi import FastAPI
from seeders.students_seeder import seed_student
# from database import db

app = FastAPI()
# Panggil Seeder
seed_student()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
