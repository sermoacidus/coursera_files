wmes=input('Enter file name,please: ')
try:
    intext=open(wmes)
except:
    print('Sorry,incorrect file name,exiting...')
    quit()
for char in intext:
    char=char.upper()
    print(char.rstrip())
#print(intext)
