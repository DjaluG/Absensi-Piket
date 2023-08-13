from database.db import db_connection
students_collection = db_connection()['students']

def seed_student():
    items_to_insert = [
        {"nis": "2", "nama" : "Test", "rombel" : "TJKT-XII", "rayon" : "Cicurug 4"}
    ]

    for item in items_to_insert:
        existing_data = students_collection.find_one({"nis": item['nis']})

        if not existing_data:
            students_collection.insert_one(item)
            print(f"Data for nis: {item['nis']} inserted")
        else:
            print(f"Data for nis: {item['nis']} already exists.")
