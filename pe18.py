f = open('pe18array.txt')
L=[]

for line in f:
    L+=[line.rstrip().split(' ')]   

for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j]=int(L[i][j])

while len(L)>1:
    for j in range(len(L[-2])):
        L[-2][j]+=max(L[-1][j],L[-1][j+1])
    L.pop(-1)

print('The biggest sum is equal to %d' % L[0][0])



