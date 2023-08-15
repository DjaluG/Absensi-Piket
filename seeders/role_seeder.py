from database.db import db_connection
role_collection = db_connection()['role']

def seed_role():
    items_to_insert = [
        {"id": 1, "title": "admin"},
        {"id": 2, "title": "pengawas"},
    ]

    for item in items_to_insert:
        existing_data = role_collection.find_one({"title": item['title']})

        if not existing_data:
            role_collection.insert_one(item)
            print(f"Data for role: {item['title']} inserted")
        else:
            print(f"Data for role: {item['title']} already exists.")