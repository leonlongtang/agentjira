import pymongo
import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['myjira']
collection = db['agents']

agentSchema = {
    'name': str,
    'description': str,
    'tasks': list,
    'role': str,
    'created_at': datetime.datetime.now(),
    'updated_at': datetime.datetime.now()
}

def get_agents():
    return collection.find()

def add_agent(agent):
    collection.insert_one(agent)

def update_agent(agent):
    collection.update_one({'_id': agent._id}, {'$set': agent.to_dict()})

def delete_agent(agent):
    collection.delete_one({'_id': agent['_id']})

def clear_agents():
    collection.delete_many({})

