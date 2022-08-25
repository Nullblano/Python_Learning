import xml.etree.ElementTree as ET
import urllib.request

url = "https://py4e-data.dr-chuck.net/comments_1598212.xml"

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
tag = tree.findall('comments/comment')

# everything below I added
numlst = []
for name in tag:
    numlst.append(int(name.find('count').text))

print('Sum:', sum(numlst))
print('Count:', len(tag))
