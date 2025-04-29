import urllib
import urllib.request
import urllib.robotparser
import re
from html import unescape 


url="https://www.google.com"
request = urllib.request.urlopen(url)
collections_of_tags = [
    'type="hidden"',
    'type="file"'
]
meta = []

if request.status == 200:
    response_body: bytes = request.read()
    response_headers: tuple = request.getheaders()
    body_decode = response_body.decode('ISO8859-1')
    body_unescape = unescape(body_decode) 
    
if body_unescape:
    let = []
    for tag in collections_of_tags:
        find_tag = re.findall(tag, body_unescape)
        if len(find_tag) > 0:
            { "tag": tag, "elem": len(tag) }