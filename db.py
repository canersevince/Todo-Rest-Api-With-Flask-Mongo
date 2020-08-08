import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


def mongo(action, user=None):
    if user is None:
        print('User not provided.')
        return 'User not provided.'

    atlas = pymongo.MongoClient(os.getenv('MONGO'))
    db = atlas['TodoApp']
    collection = db['Users']

    if action == "add":
        for x in collection.find({}, {"name": user['name']}):
            print(x)
            if x:
                return "Exists"
            else:
                created = collection.insert_one(user)
                return "Created"
    elif action == "add_todo":
        q = {"email": user['email']}
        nv = {"$set": {"todos": user['todos']}}
        print(nv)
        collection.update_one(q, nv)
        for x in collection.find({}, {"name": user['name']}):
            print(x)
            return "Updated list"
