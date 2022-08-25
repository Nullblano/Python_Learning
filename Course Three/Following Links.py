# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1:
    url = "https://py4e-data.dr-chuck.net/known_by_Jerome.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# everything below I added
count = input('Enter count: ')
position = input('Enter position: ')
print('Retrieving:', url)

names = list()

# The iteration
for i in range(int(count)):
    tags = soup('a')
    urlpos = tags[int(position) - 1]
    url = urlpos.get('href', None)
    print('Retrieving:', url) # and then open the target URL in each page
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
