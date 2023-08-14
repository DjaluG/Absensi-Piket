from fastapi import FastAPI
from seeders.students_seeder import seed_student
# from database import db
from piket_api import api
from ctm import ctm

app = FastAPI()
# Panggil Seeder
seed_student()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
app.include_router(api.router, tags=['api'], prefix='/list')
app.include_router(ctm.app, tags=['ctm'], prefix='/ctm/v1')
