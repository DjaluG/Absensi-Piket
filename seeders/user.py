from database.db import db_connection
# from models.User import UserRole
user_collection = db_connection()['auth']


def user_login():
    user_login = [
        {'name': 'admin1', 'password': hash('piket')}
    ]
    # 'role': UserRole

    for item in user_login:
        existing_data = user_collection.find_one({"name": item['name']})

        if not existing_data:
            user_collection.insert_one(item)
            print(f"Data for login: {item['name']} inserted")
        else:
            print(f"Data for login: {item['name']} already exists.")
