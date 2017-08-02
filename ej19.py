# pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/gato")
def gato():
    return """
        <video width='400' controls>
            <source src='http://mirrorblender.top-ix.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_stereo.ogg' type='video/ogg'>
            Your browser does not support HTML5 video.
        </video>
    """

app.run() # app.run(port=5001)