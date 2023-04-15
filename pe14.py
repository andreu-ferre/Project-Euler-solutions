def collatz(n):
    if n % 2 == 0:
        res = (n // 2)
    else:
        res = (3*n+1)
    return res
def cycl(m):
    l=1
    while m != 1:
        m=collatz(m)
        l+=1
    return l

curr=1
longest=0
number=1
for i in range(2,1000001):
    curr = cycl(i)
    if curr>longest:
        longest=curr
        number=i

print('The longest cycle has length %d and is created by number %d' % (longest, number))

        
