hrs=input('How many hours have u worked,fellas?:')
rate=input('What is rate?')
try:
    hrs=float(hrs)
    #print('Is it right?',hrs)
    rate=float(rate)
    uprate=rate*1.5
    hinw=40.0
    if hrs<=hinw:
        print(hrs*rate)
    else:
        extrahours=hrs%40
        print(hinw*rate+extrahours*uprate)
except:
    print('Try again,thats not a number')
