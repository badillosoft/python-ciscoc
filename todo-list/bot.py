from pymongo import MongoClient

cli = MongoClient()
db = cli.cisco

def get_tasks():
    return db.tasks.find()

def create_task(description):
    db.tasks.insert_one({
        "description": description,
        "complete": False
    })