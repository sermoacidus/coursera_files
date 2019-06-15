import re
sum=0.0
listok=list()
#listokf=list()
kon=open('фыызщкуучз.txt')
#print(kon)
for line in kon:
    line=line.strip()
    #print(line)
    x=re.findall('[0-9]+',line)
    #print(x)
    if len(x)>0:
        #print(x)
        for qnt in x:
            #print(qnt)
            #print('NAYAAA',qnt,'NYAAA')
            qnt1=float(qnt)
            #print(qnt1)
            listok.append(qnt1)
            sum=sum+qnt1
print(sum)
#print(listok)
#for n1 in listok:
    #sum=sum+n1
#print(sum)
        #listok.append(x)
#print(listok)
#print(listok[0])
#        for elem in listok:
#            elem=float()
#            listokf.append(elem)
    #print(x)
#print(listok)
#print(listokf)
#for char in listok:
#    print(char)
#    char=float()
#    sum=sum+char
#print(sum)
