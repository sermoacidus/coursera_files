john={}
count=0
bigkey=None
bigvalue=0
entrance=input('enter the file name,plz: ')
try:fajlik=open(entrance)
except:
    print('ok,ill do it 4 ya...')
    fajlik=open('mbox-short.txt')
#print(fajlik)
nvssl=list()
for line in fajlik:
    line=line.rstrip()
    if line.startswith('From '):
        count=count+1
        kon=line.split()
        kon=kon[5]
        kon=kon[0:2]
        nvssl.append(kon)
#print(nvssl)
        #print(kon)
        #print(line[1])
#print(count)
for time in nvssl:
    john[time]=john.get(time,0)+1
perech=list()
#print(john)
for k,v in john.items():
    #print(k,v)
    perech.append((k,v))
perech.sort(inverse=true)
for k,v in perech:
    print(k,v)
#print(perech)
#print(bigkey,bigvalue)
