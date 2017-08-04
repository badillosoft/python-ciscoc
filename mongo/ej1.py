from pymongo import MongoClient

cli = MongoClient()

db = cli.cisco # cli["cisco"]

# personas = db["personas"]

db.personas.insert_one({
    "nombre": "Python",
    "edad": 12,
})

db.personas.insert_many([
    {
        "nombre": "Persona 1",
        "edad": 21,
    },
    {
        "nombre": "Persona 2",
        "edad": 16,
    },
    {
        "nombre": "Persona 3",
        "edad": 17,
    },
])

cli.close()