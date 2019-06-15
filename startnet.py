import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

vigryz=urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_237871.html',context=ctx).read()
soup=BeautifulSoup(vigryz, 'html.parser')

#listik=list()
sum=0
tags=soup('tr')
for tag in tags:
    #print('TAG:', tag)
    #print(type(tag))
    tag=str(tag)
    x=re.findall('"comments">(.+?)</span>',tag)
    if len(x)<1:
        continue
    #print(type(x))
    for xin in x:
        xin=int(xin)
    #print(xin)
    sum=sum+xin
    #listik.append(x)
    #print(x)
print(sum)
    #print('td: ', tag.get('td', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

#agon=dict()
#for polos in vigryz:
    #whatev=polos.decode().strip()
    #print(whatev)
    #for whate in whatev:
        #agon[whate]=agon.get(whate,0)+1
#print(agon)

#while True:
#    data=mysocket.recv(512)
#    if len(data)<1:
#        break
#    print(data.decode(),end='')
#mysocket.close()
