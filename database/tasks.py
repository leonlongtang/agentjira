from pymongo import MongoClient
import datetime
client = MongoClient('mongodb://localhost:27017/')
db = client['myjira']
collection = db['tasks']

taskSchema = {
    'title': str,
    'description': str,
    'status': str,
    'assignee': str,
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now()
}

def get_tasks():
    return collection.find()

def add_task(task):
    collection.insert_one(task)

def update_task(task):
    collection.update_one({'_id': task._id}, {'$set': task.to_dict()})

def delete_task(task):
    collection.delete_one({'_id': task._id})

def clear_tasks():
    collection.delete_many({})
