spisok=list()
while True:
    inp=input('ADD NUMBERS TO THE LIST: ')
    if inp == 'done':
        break
    try:
        value=float(inp)
    except:
        print('DONT LIE! ITS NOT A NUMBER! TRY AGAIN')
        continue
    spisok.append(value)
print(spisok)
print('TOT:',sum(spisok),'/AMOUNT OF ITEMS:',len(spisok))
try:
    average=sum(spisok)/len(spisok)
except:
    print('NO DATA FOUND 404')
try:
    print('AVERAGE IS',average)
except:
    quit()
