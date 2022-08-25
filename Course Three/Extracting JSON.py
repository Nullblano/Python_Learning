import json
import xml.etree.ElementTree as ET
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_1598213.json"

address = urllib.request.urlopen(url)
data = address.read()

info = json.loads(data)
info = info["comments"]

# everything below this I added
total = 0

for item in info:
    total = total + int(item['count'])

print('Final Sum:', total)
