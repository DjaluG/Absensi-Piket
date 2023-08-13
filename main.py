from fastapi import FastAPI
<<<<<<< HEAD
from seeders.students_seeder import seed_student
# from database import db
=======
# from database import db
from piket_api import api
>>>>>>> 52b3c575409147a8f90b42069e8501f0dce36132

app = FastAPI()
# Panggil Seeder
seed_student()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
<<<<<<< HEAD
=======
app.include_router(api.router, tags=['api'], prefix='/items/v1')
>>>>>>> 52b3c575409147a8f90b42069e8501f0dce36132
