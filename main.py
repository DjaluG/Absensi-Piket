from fastapi import FastAPI
from seeders.students_seeder import seed_student
from seeders.user import user_login
from seeders.role_seeder import seed_role
# from database import db
from piket_api import api
from ctm import ctm
from auth import auth

app = FastAPI()
# Panggil Seeder
seed_student()
user_login()
seed_role()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
app.include_router(api.router, tags=['api'], prefix='/list')
app.include_router(ctm.app, tags=['ctm'], prefix='/ctm')
app.include_router(auth.app, tags=['auth'], prefix='/auth')
