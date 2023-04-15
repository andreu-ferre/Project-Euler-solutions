from pe41 import isprime

def numprimes(a, b):
	
	for n in range(abs(b)):
		poly = n ** 2 + a * n + b
		if not isprime(abs(poly)):
			return n
	
	return abs(b)-1

if __name__ == '__main__':

	B = []
	for n in range(-1000,1001):
		x = abs(n)
		if isprime(x) and x > 40:
			B.append(n)
		
	A = [n for n in range(-999,1000)]
	primes = 1
	for x in A:
		for y in B:
			d = numprimes(x, y)
			if d > primes:
				primes = d
				res = x * y
				
	print('The desired product is equal to %d' % res)
			
		