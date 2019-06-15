wmes=input('Enter file name,please: ')
try:
    intext=open(wmes)
except:
    print('Sorry,incorrect file name,exiting...')
    quit()
counting=0.0
tot=0.0
for char in intext:
    if not char.startswith('X-DSPAM-Confidence'):
        continue
    posi=char.find(':')
    ldef=char[posi+1:]
    ldef=ldef.lstrip()
    ldef=float(ldef)
    tot=tot+ldef
    counting=counting+1
    #print(char.rstrip())
#print(counting)
print('Average spam confidence:',tot/counting)
