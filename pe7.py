L=[2]
c=L[0]
d=1
s=len(L) 
n=input('Type the place of the prime number you want to know:')
bound=int(n)
while len(L)<bound:
    for i in range(c+1,2*c+2):
        for j in L:
            if i % j == 0:
                d=j
                break
        if d==1:
            L.append(i)
            c=i
        else:
            d=1
        if len(L)== bound: break

print(len(L))
if L[-1]==L[bound-1]:
    print('Debugged')
print(L[bound-1])
