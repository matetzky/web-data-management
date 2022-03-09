import xml.etree.ElementTree as ET

tree = ET.parse('paris.html')
root = tree.getroot()

for k in root.findall(".//a"):
	print(k.text)

for k in root.findall(".//img[@alt]"):
	print(k.attrib['alt'])


