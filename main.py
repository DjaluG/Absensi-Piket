from fastapi import FastAPI
# from database import db
from piket_api import api

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(db.app, tags=['db'], prefix='/items/v1')
app.include_router(api.router, tags=['api'], prefix='/items/v1')
