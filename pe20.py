d=1
nst = input('Type the number whose factorial you are interested in: ')
n=int(nst)
for i in range(1,n+1): d*=i

l=str(d)
ans = sum(int(l[i]) for i in range(len(l)))

print('The sum of the digits of %d! is equal to %d' % (n, ans))
