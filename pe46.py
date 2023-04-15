from pe41 import isprime
import math

def isgoldbach(n):
	j = 0
	while primeL[j] < n:
		x = (n-primeL[j]) // 2
		y = math.sqrt(x)
		z = y-int(y)
		if z == 0:
			return True
		j += 1
		
	return False
		
	

if __name__ == '__main__':
	primeL=[2]
	for n in range(3, 10 ** 6, 2):
		if isprime(n): primeL.append(n)
		
	for n in range(33, 10 ** 6, 2):
		if not isprime(n) and not isgoldbach(n):
			print("The first number that fails Goldbach's conjecture is %d" % n)
			break
	
	
		
			