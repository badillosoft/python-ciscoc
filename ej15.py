import urllib2

url = "http://placehold.it/200x200"

filename = "salida.jpg"
 
request = urllib2.urlopen(url)

f = file(filename, "w")

f.write(request.read())

f.close()