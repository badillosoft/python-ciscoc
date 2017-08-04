from pymongo import MongoClient

cli = MongoClient()
db = cli.cisco

def contacts():
    return db.contacts.find()

def create_contact(name, email, picture):
    print "Create contact: <%s> <%s> <%s>" % (name, email, picture)
    if not name or not email:
        return
    db.contacts.insert_one({
        "name": name,
        "email": email,
        "picture": picture
    })

def login(username, password):
    return db.users.find_one({ "username": username, "password": password })