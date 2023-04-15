a=600851475143
import math
b=int(math.sqrt(a))
print(b)
c=1
d=1
for i in range(1,b+1):
    for j in range(1,int(math.sqrt(i)+1)):
        if i % j == 0:
            c=j
    #print(c)
    if a % i == 0 and c == 1:
        d=i
#if (a/d)>d:
#    d=(a/d)
print(d)

