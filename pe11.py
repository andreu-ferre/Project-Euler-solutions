"""
The first two fors read a matrix from a text file and return it as a list of actual integers
Susceptible to be made a function:
def mreader(minput):
    L=[]
    for line in minput:
        L+=[line.rstrip().split(' ')]
    for i in range(len(L)):
        for j in range(len(L[i])):
        L[i][j]=int(L[i][j])
    return L
"""
f = open('pe11array.txt')
L=[]

for line in f:
    L+=[line.rstrip().split(' ')]   

for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j]=int(L[i][j])

maxprod=0
prod=1
for i in range(len(L)):
    for j in range(len(L[i])):
        if j<16:
            prod*=L[i][j]*L[i][j+1]*L[i][j+2]*L[i][j+3]
            maxprod=max(prod,maxprod)
            prod=1
        if i<16:
            prod*=L[i][j]*L[i+1][j]*L[i+2][j]*L[i+3][j]
            maxprod=max(prod,maxprod)
            prod=1
        if i<16 and j < 16:
            prod*=L[i][j]*L[i+1][j+1]*L[i+2][j+2]*L[i+3][j+3]
            maxprod=max(prod,maxprod)
            prod=1
        if  i>=3 and j<16:
            prod*=L[i][j]*L[i-1][j+1]*L[i-2][j+2]*L[i-3][j+3]
            maxprod=max(prod,maxprod)
            prod=1

print('The biggest product in the array is equal to %d' % maxprod)
        



