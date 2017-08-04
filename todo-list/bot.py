from pymongo import MongoClient

cli = MongoClient()
db = cli.cisco

def get_tasks():
    return db.tasks.find()