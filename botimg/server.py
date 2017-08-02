from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",
        message="Hola mundo",
        pictures=[
            "https://foro.hackxcrack.net/index.php?action=dlattach;attach=3441;type=avatar",
            "https://avatars3.githubusercontent.com/u/6743118?v=4&s=400",
            "http://www.cats.org.uk/uploads/images/featurebox_sidebar_kids/grief-and-loss.jpg",
        ]
    )

app.run()