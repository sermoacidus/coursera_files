import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import xml.etree.ElementTree as ET

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE



xweb=input('What site: ')
vigryz=urllib.request.urlopen(xweb,context=ctx).read()
vigryz=vigryz.decode()
#vigryz=vigryz.rstrip()
#for k in vigryz:
#    k=str(k)
#    print(k)
#print(vigryz,type(vigryz))

#iksemel=input('vvedi xml')
#vvod=("'''"+vigryz+"'''")
sum=0

#print(vvod)
saker=ET.fromstring(vigryz)
#print(saker)
listik=saker.findall('comments/comment')
#print(len(listik))
for item in listik:
    #print(item)
    #print('Name',item.find('name').text)
    x=item.find('count').text
    #print('Count',x)
    sum=sum+int(x)
print(sum)
    #print(y)
 
