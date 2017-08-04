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
    "$or": [
        {
            "edad": 18
        },
        {
            "nombre": "Persona 2"
        }
    ]
}

for p in db.personas.find(query):
    print p

cli.close()