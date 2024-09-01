import json
from pymongo import MongoClient

def load_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['kimo_db']
    collection = db['courses']

    with open('../data/courses.json') as f:
        courses = json.load(f)

    collection.drop() 
    collection.create_index([("name", 1)])
    collection.create_index([("date", -1)])
    collection.create_index([("rating", -1)])
    
    collection.insert_many(courses)

if __name__ == "__main__":
    load_data()
