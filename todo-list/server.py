from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    tasks = [
        {
            "description": "Ir al cine",
            "complete": True
        },
        {
            "description": "Hacer el proyecto :(",
            "complete": False
        }
    ]

    return render_template("list.html", tasks=tasks)

app.run()