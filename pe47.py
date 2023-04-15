from pe41 import isprime
import math
"""
n // 2 bound easily improvable! As is, runs in 40 seconds.
"""
def consecutive(n):

	x = n + 1
	y = n + 2
	z = n + 3
	L = [n, x, y, z]
	t = int(math.sqrt(n))
	for m in L:
		primes = 0
		for j in primeL:
			if m % j == 0:
				primes += 1
			if primes == 4:
				break
			if j > n // 2:
				break
				
		if primes < 4:
			return False

	return True		
		

if __name__ == '__main__':
	
	primeL = [2]
	for n in range(3, 10 ** 6, 2):
		if isprime(n):
			primeL.append(n)
			

	for n in range(2, 10 ** 6):
		if consecutive(n):
			print('The first number where the property occurs is %d' % n)
			break