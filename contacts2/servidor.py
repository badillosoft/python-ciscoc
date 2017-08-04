from flask import Flask, render_template
from pymongo import MongoClient

cli = MongoClient()
db = cli.cisco

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
        nombre="Alan",
        coleccion=db.pictures.find())

app.run()