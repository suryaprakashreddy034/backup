
text = 'w'
num=10

ascii = ord(text)

ran1=range(65,90)
ran2=range(97,122)

if ascii in ran1:
    newascii=ascii+num
    if newascii>90:
        newascii=newascii-26
        newchar=chr(newascii)
    else:
        newchar=chr(newascii)

    print(newchar)
   

elif ascii in ran2:
    newascii=ascii+num
    if newascii>122:
        newascii=newascii-26
        newchar=chr(newascii)
    else:
        newchar=chr(newascii)
    print(newchar)