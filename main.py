from fastapi import FastAPI
from seeders.students_seeder import seed_student
# from database import db
from piket_api import api


app = FastAPI()
# Panggil Seeder
seed_student()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
app.include_router(api.router, tags=['api'], prefix='/items/v1')
