a=1; b=1; c=1; L=1
for i in range(1,250):
    for j in range(i+1,1000-333):
        L=(10 ** 3)*(i+j)-i*j
        if L == 500000:
            a=i
            b=j

c=1000-(a+b)
print(c)
d=a*b*c
print(d)

            
