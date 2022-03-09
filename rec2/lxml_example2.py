import requests 
import lxml.html

res = requests.get("http://google.com") 
doc = lxml.html.fromstring(res.content)
for t in doc.xpath("//a[contains(@href, 'youtube')]/@href"):
	print(t)


