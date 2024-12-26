import pymongo
from pymongo import MongoClient

# Підключення до бази даних MongoDB
client = MongoClient("mongodb+srv://cat_database:GoIT19101990@cluster0.yulx1.mongodb.net/")  
db = client["cat_database"]  # Ім'я бази даних
collection = db["cats"]  # Ім'я колекції

# Функція для створення документа (Create)
def create_cat(collection, name, age, features):
    document = {
        "_id": ObjectId("60d24b783733b1ae668d4a77"),
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }
    result = collection.insert_one(document)
    print(f"Created document with ID: {result.inserted_id}")

# Функція для читання всіх документів (Read)
def read_all_cats(collection):
    documents = list(collection.find())
    for doc in documents:
        print(doc)

# Функція для читання кота за ім'ям
def read_cat_by_name(collection, name):
    result = collection.find_one({"name": name})
    return result

# Функція для оновлення віку кота (Update)
def update_cat_age(collection, name, new_age):
    collection.update_one(
        {"name": name},
        {"$set": {"age": new_age}}
    )
    print(f"Updated age for {name} to {new_age}")

# Функція для додавання нової характеристики коту
def add_feature_to_cat(collection, name, feature):
    collection.update_one(
        {"name": name},
        {"$addToSet": {"features": feature}}
    )
    print(f"Added feature '{feature}' to {name}")

# Функція для видалення кота за ім'ям (Delete)
def delete_cat_by_name(collection, name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted document for {name}")
    else:
        print(f"No document found for {name}")

# Функція для видалення всіх документів
def delete_all_cats(collection):
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} documents")

# Головна функція для тестування
if __name__ == "__main__":
    collection = connect_to_db()
    if collection:
        # Додавання кота
        create_cat(collection, "barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
        create_cat(collection, "murzik", 2, ["чорний", "грається з мишами"])
        
        # Читання всіх котів
        print("\nВсі коти:")
        read_all_cats(collection)
        
        # Читання кота за ім'ям
        print("\nПошук кота 'barsik':")
        read_cat_by_name(collection, "barsik")
        
        # Оновлення віку
        print("\nОновлення віку кота 'barsik':")
        update_cat_age(collection, "barsik", 4)
        
        # Додавання нової характеристики
        print("\nДодавання характеристики коту 'barsik':")
        add_feature_to_cat(collection, "barsik", "любить молоко")
        
        # Видалення кота
        print("\nВидалення кота 'murzik':")
        delete_cat_by_name(collection, "murzik")
        
        # Видалення всіх котів
        print("\nВидалення всіх котів:")
        delete_all_cats(collection)
