import requests 
import lxml.html 

r = requests.get("http://en.wikipedia.org/wiki/Israel") 
doc = lxml.html.fromstring(r.content)
for t in doc.xpath("//img[not(@alt = '')]"):
	print(t.attrib["alt"])

## other option:

for t in doc.xpath("//img[not(@alt = '')]/@alt"):
	print(t)




