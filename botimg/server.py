# _*_ coding: utf-8 _*_
from flask import Flask, request, render_template
import botimg as bot

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("q")
    pictures = bot.pictures(query)
    message = u"No encontré ningún resultado :("
    n = len(pictures)
    if n > 0:
        message = u"Para [%s] encontré %d resultados :)" % (query, n)
    return render_template("home.html",
        message=message,
        pictures=pictures
    )

app.run()