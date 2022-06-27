a=[1,2,3,'d','f','g','*']

for i in a:
    i=str(i)
    if i.isnumeric() or i.isalpha():
        continue
    else:
        print(i)