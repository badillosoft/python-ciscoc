import urllib2

url = "https://duckduckgo.com/?q=tomate&t=h_&ia=web"

request = urllib2.urlopen(url)

print request.read()