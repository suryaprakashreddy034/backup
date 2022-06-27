n=4

l1=[]

for i in range(0,n):
    a=input()
    l1.append(a)



K = 1
l2=[]
for test_str in l1:
    res = []
    for idx in range(0, len(test_str), K):
        # converting to int, after slicing
        res.append(int(test_str[idx: idx + K]))

    l2.append(res)

    


sumall=[]
for i in l2:
    oddsum = sum(i)
    sumall.append(oddsum)

print(sumall)