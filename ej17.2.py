import urllib2
import re

url = "https://duckduckgo.com/?q=hello%20world&ia=web"

request = urllib2.urlopen(url)

content = request.read()

pattern = "https?:[\:\/\w\-\.\?\&\=]+\.jpg"

def T(m):
    return "<img src='%s'>" % m.group(0)

tags = map(T, re.finditer(pattern, content))

print tags

f = open("salida.html", "w")

for tag in tags:
    f.write(tag)
    
f.close()