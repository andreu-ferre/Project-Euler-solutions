def legendreformula(n, p):
	i = 1
	m = p
	res = 0
	while n // m > 0:
		res += n // m
		m *= p
		
	return res

num = 200000

numer2 = legendreformula(num, 2)
numer5 = legendreformula(num, 5)
#print(numer2, numer5)
res = 0
for i in range(num):
	if legendreformula(i, 2)>numer2-12: 
		if legendreformula(i, 5)>numer5-12:
			print(i)
			res += 1
			
print('The total number is %d' % res)
		
		