from database.db import db_connection
day_collection = db_connection()['days']

def seed_day():
    items_to_insert = [
        {"id": 1, "nama": "Senin"},
        {"id": 2, "nama": "Selasa"},
        {"id": 3, "nama": "Rabu"},
        {"id": 4, "nama": "Kamis"},
        {"id": 5, "nama": "Jumat"},
    ]

    for item in items_to_insert:
         existing_data = day_collection.find_one({"nama": item['nama']})

         if not existing_data:
            day_collection.insert_one(item)
            print(f"Data for role: {item['nama']} inserted")
         else:
            print(f"Data for role: {item['nama']} already exists.")
