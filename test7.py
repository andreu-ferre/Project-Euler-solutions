L=[2]
c=L[0]
d=1    

for i in range(c+1, 2*c+2):
    for j in L:
        if i % j == 0:
            d=j
        if d>1: break
        if d == 1:
            L.append(i)
            c=L[-1]
            print(c)
        else:
            d=1

