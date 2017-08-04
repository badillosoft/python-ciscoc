from pymongo import MongoClient

cli = MongoClient()

db = cli.cisco

query = {
    "nombre": "Persona 1"
}

for p in db.personas.find(query):
    print p

cli.close()