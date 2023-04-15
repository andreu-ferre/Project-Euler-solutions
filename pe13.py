s=0
j=0
f = open('pe13num.txt')

for line in f:
    s+=int(line.rstrip())

l=str(s)
#print(l)
for i in range(10):
    print(l[i])


