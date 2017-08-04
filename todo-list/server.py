from flask import Flask, render_template, request
import bot

app = Flask(__name__)

@app.route("/")
def home():
    desc = request.args.get("desc")
    bot.create_task(desc)
    return render_template("list.html", tasks=bot.get_tasks())

app.run()