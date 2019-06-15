hrs = input("Enter Hours:")
h = float(hrs)
rate=10.50
uprate=rate*1.5
hinw=40.0
if h<=hinw:
    print(h*rate)
else:
    extrahours=h%40
    print(hinw*rate+extrahours*uprate)
