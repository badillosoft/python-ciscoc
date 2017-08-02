import urllib2
import re

url = "https://duckduckgo.com/?q=hello%20world&ia=web"

request = urllib2.urlopen(url)

content = request.read()

pattern = "https?:[\:\/\w\-\.\?\&\=]+\.jpg"

def T(m):
    return "<img src='%s' style='max-width:200px'>" % m.group(0)

tags = map(T, re.finditer(pattern, content))

print tags

f = open("salida.html", "w")

f.write("<ul>")
for tag in tags:
    f.write("<li>")
    f.write(tag)
    f.write("</li>")
f.write("</ul>")
    
f.close()