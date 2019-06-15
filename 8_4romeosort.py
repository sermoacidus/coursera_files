kasha=input('Enter file name:')
fayl=open(kasha)
kres=list()
for line in fayl:
    words=line.split()
    #print(words)
    for n in words:
        if n not in kres:
            kres.append(n)
kres.sort()
print(kres)
