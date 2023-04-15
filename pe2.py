a=1
b=2
c=0
evensum=0
cutoff=0
for i in range(1,10000):
    c=a
    a=b
    b+=c
    if c>4000000:
        cutoff=i
        break
a=1
b=2
c=0
for i in range(1,cutoff+1):
    c=a
    a=b
    b+=c
    if i % 3 == 2:
        evensum+=c

print(evensum)
