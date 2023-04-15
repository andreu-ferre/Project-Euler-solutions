s=1
nst = input('What power of 2 are you interested in?')
n = int(nst)
for i in range(n):
    s+=s

#print(s)
l=str(s)
ans = sum(int(l[i]) for i in range(len(l)))
print('The sum of the digits of 2 to the power %d is equal to %d' % (n, ans))
