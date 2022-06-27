

n1=1
test_str =str(2514795)


# initializing substring

K = 1
res = []
for idx in range(0, len(test_str), K):
    # converting to int, after slicing
    res.append(int(test_str[idx: idx + K]))


odd=[]
even=[]
for num in res:
    if num % 2 != 0:
        odd.append(num)
    else:
        even.append(num)


oddsum = sum(odd)
evensum= sum(even)

totaldis=oddsum*evensum
print(totaldis)
