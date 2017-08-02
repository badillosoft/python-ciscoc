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

print pictures("monkey")
print "-" * 40
print pictures("car")
print "-" * 40
print pictures("cat dog")

def pictures_html(pics):
    html = "<ul>"

    for url in pics:
        html += "<li>"
        html += "<img style='max-width:100px' src='%s'>" % url
        html += "</li>"

    html += "</ul>"

    return html

print pictures_html(pictures("donkey"))