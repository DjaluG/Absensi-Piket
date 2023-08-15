from fastapi import APIRouter, HTTPException, Depends
from models.Student import Student
from pydantic import parse_obj_as
from database.db import db_connection
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from models.User import User
from auth.auth_handler import get_current_user
from database.db import db_connection
# import csv
# from pymongo import MongoClient

router = APIRouter()
auth_collection = db_connection()['auth']
collection = db_connection()['students']


@router.get('/students')
async def get_all_students():

    students = collection.find()
    student_list = []
    for student in students:
        # Convert ObjectId to string
        student['_id'] = str(student['_id'])
        student_list.append(student)

    return student_list

# Delete


@router.delete('/students/{student_id}')
async def delete_students(student_id: str, current_user: User = Depends(get_current_user)):
    if current_user.role_id != 1:
        raise HTTPException(status_code=403, detail="Forbidden")

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
async def update_student(student_id: str, updated_student: Student, current_user: User = Depends(get_current_user)):

    if current_user.role_id != 1:
        raise HTTPException(status_code=403, detail="Forbidden")

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


# Sudah piket
@router.post('/success/{student_id}')
async def mark_picket(student_id: str):
    collection = db_connection()['students']

    # Temukan data berdasarkan ObjectId
    result = collection.find_one({"_id": ObjectId(student_id)})

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # ubah dict menjadi model
    student = parse_obj_as(Student, result)

    student.status = True

    updated_result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.dict()}
    )

    if updated_result.modified_count == 1:
        return {"message": f"Student marked as piket success"}
    else:
        return {"message": "No changes were made"}

# Batalkan sudah piket


@router.post('/cancel/{student_id}')
async def mark_picket(student_id: str):
    collection = db_connection()['students']

    # Temukan data berdasarkan ObjectId
    result = collection.find_one({"_id": ObjectId(student_id)})

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # ubah dict menjadi model
    student = parse_obj_as(Student, result)

    student.status = False

    updated_result = collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.dict()}
    )

    if updated_result.modified_count == 1:
        return {"message": f"Student marked as unpiket success"}
    else:
        return {"message": "No changes were made"}
