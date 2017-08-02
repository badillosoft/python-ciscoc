import urllib2
import re

url = "https://duckduckgo.com/?q=mono&ia=web"

request = urllib2.urlopen(url)

content = request.read()

pattern = "https?:[\:\/\w\-\.\?\&\=]+\.jpg"

for m in re.finditer(pattern, content):
    print m.group(0)