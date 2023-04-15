nums=0
totsum=0
fL=[1]
d=1
for i in range(1,10):
    d*=i
    fL+=[d]

for i in range(3,int(2.91E7)):
    for c in str(i):
        nums+=fL[int(c)]
    if nums == i:
        totsum+=i
    nums=0

print('The total sum is equal to %d' % totsum)
        

