# _*_ coding: utf8 _*_
from pymongo import MongoClient

cli = MongoClient()

db = cli.cisco

# gt >
# gte >=
# lt <
# lte <=
# eq ==
# ne !=

query = {
    "edad": {
        "$gte": 18
    }
}

for p in db.personas.find(query):
    print p

cli.close()