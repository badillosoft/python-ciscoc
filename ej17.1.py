import urllib2
import re

url = "https://duckduckgo.com/?q=mono&ia=web"

request = urllib2.urlopen(url)

content = request.read()

pattern = "https?:[\:\/\w\-\.\?\&\=]+\.jpg"

def T(m):
    return "<img src='%s'>" % m.group(0)

urls = map(T, re.finditer(pattern, content))

print urls