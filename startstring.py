text='X-DSPAM-Confidence:        0.8475'
spos=text.find(':')
text=text[spos+1:]
text=text.lstrip()
text=float(text)
#resul=text.rstrip(spos+1)
print(text)
