d=1
tsum=2
n=input('Type the bound for the prime numbers:')
bound=int(n)
import math
for i in range(3,bound,2):
    for j in range(2,(round(math.sqrt(i))+5)):
        if i % j == 0 and j<i:
            d=j
        if d>1: break
    if d == 1:
        tsum+=i
    else:
        d=1

print('The sum of primes less than %d' % bound, 'is equal to %d' % tsum)


