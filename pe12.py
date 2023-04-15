# This divisors function is godawful. Needs to be improved!

def divisors(m):
	res = 0
	for j in range(1,m+1):
		if m % j == 0:
			res += 1
			
	return res

div = 0
n = 1
while div <= 500:
	if n % 2 == 0:
		div = divisors(n//2)*divisors(n+1)
	else:
		div = divisors(n)*divisors((n+1)//2)
	
	print(div)	
	n += 1
	print(n)
res = (n-1)*n//2

print('The first highly divisible number is %d' % res)