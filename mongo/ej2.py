from pymongo import MongoClient

cli = MongoClient()

db = cli.cisco

for p in db.personas.find():
    print p

cli.close()