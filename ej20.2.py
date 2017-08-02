import urllib2
import re

def pictures(query):
    url = "https://duckduckgo.com/?q=%s&ia=web" % query
    request = urllib2.urlopen(url)
    content = request.read()
    # pattern = "https?://(\w+\.\?)+(:\d+)?[\/\w\.\-\_\?\&\=].jpg"
    pattern = "https?:[\:\/\w\-\.\?\&\=]+\.(jpg|jpeg|png|bmp|gif)"
    pics = []
    for m in re.finditer(pattern, content):
        url_pic = m.group(0)
        pics.append(url_pic)
    return pics

def pictures_html(pics):
    html = "<ul>"

    for url in pics:
        html += "<li style='list-style-type:none'>"
        html += "<img style='display:block;float:left;height:100px;margin:10px' src='%s'>" % url
        html += "</li>"

    html += "</ul>"

    return html

############################################################
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    query = request.args.get("q")
    pics = pictures(query)
    html = pictures_html(pics)
    return html

app.run()