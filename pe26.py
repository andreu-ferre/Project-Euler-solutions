L=[n for n in range(2,1000)]

def decimals(n):
	quot = '0.'
	num = 10
	R = []
	while num % n not in R:
		quot += str(num // n)
		R.append(num % n)
		if num % n == 0: break
		num = (num % n) * 10
	
	return quot
	
def cyclength(n):
	m = decimals(n)[2:]
	while m[0] == 0:
		m = m[1:]
		
	return len(m)
	
if __name__ == '__main__':
	res = 0
	for n in range(2, 1000):
		x = cyclength(n)
		if x > res:
			res = n
			
	print('The value for which 1/d contains the longest cycle is %d' % res)
	
