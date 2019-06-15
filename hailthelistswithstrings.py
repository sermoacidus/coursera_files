fayl=open('mbox-short.txt')
count=0
for line in fayl:
    #line=line.rstrip()
    if not line.startswith('From '):
        continue
    count=count+1
    words=line.split()
    #print(words)
    email=words[1]
    #print(email)
    #kuski=email.split('@')
    print(email)
print("There were", count, "lines in the file with From as the first word")



#spisok=list()
#while True:
#    inp=input('ADD NUMBERS TO THE LIST: ')
#    if inp == 'done':
###        value=float(inp)
    #except:
#        print('DONT LIE! ITS NOT A NUMBER! TRY AGAIN')
#        continue
#    spisok.append(value)
#print(spisok)
#print('TOT:',sum(spisok),'/AMOUNT OF ITEMS:',len(spisok))
#try:
#    average=sum(spisok)/len(spisok)
#except:
#    print('NO DATA FOUND 404')
#try:
#    print('AVERAGE IS',average)
#except:
#    quit()
