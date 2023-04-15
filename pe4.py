c=0
d=0
str1=''
str2=''
L=[]
for i in range(100,1000):
    L.append(i)
L1=L[::-1]
for i in L1:
    if i % 11 == 0:
        for j in L1:
            d=i*j
            str1=str(d)
            str2=str1[::-1]
            if str1 == str2 and d>c:
                c=d

print(c)
