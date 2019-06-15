import urllib.request, urllib.parse, urllib.error
import json

gmaps = 'http://py4e-data.dr-chuck.net/json?'

api_key = 42
dop_dannye=dict()
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    dop_dannye['address'] = address
    dop_dannye['key'] = api_key
    url = gmaps + urllib.parse.urlencode(dop_dannye)

    print('Retrieving',url,sep=' ----->>>  ')

    urlop = urllib.request.urlopen(url)
    data = urlop.read().decode()
    print('Retrieved', len(data), 'characters')

    #print(data)

    try:
        js = json.loads(data)
    except:
        js = None

    #print(js)

    print('Place id=',js['results'][0]['place_id'])
    #for i in js['results'][0]['place_id']:
        #print(i)
        #try:
            #print(i['count'],type(i['count']))
            #sum=sum+i['count']
        #except:
            #print(i,'no values_===================', type(i))
            #continue

    #if not js or 'status' not in js or js['status'] != 'OK':
        #print('FAILURE================')
        #print(data)
        #continue
