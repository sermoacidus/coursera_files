hrs=input('How many hours have u worked,fellas?:')
rate=input('What is rate?')
try:
    hrs=float(hrs)
    #print('Is it right?',hrs)
    rate=float(rate)
except:
    print('Try again,thats not a number')
    quit()
uprate=rate*1.5
hinw=40.0
def computepay(hrs,rate):
    if hrs<=hinw:
        return hrs*rate
    else:
        extrahours=hrs%40
        return hinw*rate+extrahours*uprate
p=computepay(hrs,rate)
print(p)
