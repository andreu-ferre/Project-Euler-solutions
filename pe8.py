a=input('Length of string:')
b=int(a)
tsum=-5*b*b
index=0
answer=1
outfile = open('pe8ans.txt','w')
import math
L=[-5*b]
for i in range(1,10):
    L+=[round(math.log(i),1)]
file = open('pe8num.txt').read()
file=file.replace('\n','')
# number=int(file)
numlist=[]
for j in range(len(file)):
    numlist += [int(file[j])]
print(numlist, file=outfile)
for k in range(0,len(file)-b):
    d=sum(L[numlist[t]] for t in range(k,k+b))
    if d>tsum:
        tsum=d
        index=k
for i in range(b):
    answer*=numlist[index+i]
print('The answer is %d' % answer, file=outfile)

