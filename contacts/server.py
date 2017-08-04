from flask import Flask, request, render_template, session, redirect
import bot

app = Flask(__name__)

app.secret_key = 'ABCDEF1234567890@'

@app.route("/")
def home():
    if not session.has_key("login"):
        return redirect("/login")
    name = request.args.get("name")
    email = request.args.get("email")
    picture = request.args.get("picture")
    bot.create_contact(name, email, picture)
    return render_template("index.html", contacts=bot.contacts())

@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if bot.login(username, password):
            session["login"] = True
            session["username"] = username
            return redirect("/")
        message = "Invalid credentials"
    return render_template("login.html", error=message)

app.run()