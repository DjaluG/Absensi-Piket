from fastapi import APIRouter
from models.Student import Student
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from database.db import db_connection
# import csv
# from pymongo import MongoClient

router = APIRouter()


@router.get('/students')
async def get_all_students():
    collection = db_connection()['students']
    students = collection.find()
    student_list = []
    for student in students:
        # Convert ObjectId to string
        student['_id'] = str(student['_id'])
        student_list.append(student)

    return student_list

# Delete


@router.delete('/students/{student_id}')
async def delete_students(student_id: str):
    collection = db_connection()['students']
    # Temukan Id Student dan delete
    result = collection.delete_one({"_id": ObjectId(student_id)})

    if result.deleted_count == 1:
        return {"message": f"Student Succesffully deleted"}
    else:
        return {"message": f"Student  Not Found"}

# Get Id Student


@router.get('/students/{student_id}')
async def get_specific_student(student_id: str):
    collection = db_connection()['students']

    # Temukan data berdasarkan ObjectId
    result = collection.find_one({"_id": ObjectId(student_id)})

    if result:
        # Convert ObjectId to String
        result['_id'] = str(result['_id'])
        return jsonable_encoder(result)
    else:
        return {"message": "Student not found"}

# Update


@router.put('/students/{student_id}')
async def update_student(student_id: str, updated_student: Student):
    collection = db_connection()['students']
    result = collection.update_one({"_id": ObjectId(student_id)}, {
                                   "$set": updated_student.dict()})

    if result.modified_count == 1:
        return {"message": f"Student Updated"}
    else:
        return {"message": f"Student not found"}

# Create


@router.post('/students')
async def create_student(student: Student):
    collection = db_connection()['students']
    result = collection.insert_one(student.dict())

    return {"message": "Student created", "student_id": str(result.inserted_id)}
