from flask import Flask, render_template
import bot

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("list.html", tasks=bot.get_tasks())

app.run()