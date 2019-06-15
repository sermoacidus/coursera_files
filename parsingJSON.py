import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re
from bs4 import BeautifulSoup

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

sum=0

velcom = input('enter site ')
vigryz = urllib.request.urlopen(velcom,context=ctx).read()
soup=BeautifulSoup(vigryz, 'html.parser')


soup=str(soup)
#print(soup, type(soup))
#data = ("'''"+soup+"'''")
#data = str(data)
#print(data)


info = json.loads(soup)

#print(info,type(info))

for i in info['comments']:
    try:
        #print(i['count'],type(i['count']))
        sum=sum+i['count']
    except:
        print(i,'no values_===================', type(i))
        continue

print(sum)
