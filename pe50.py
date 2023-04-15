from pe41 import isprime

def maxprimes(p, bound):
	ub = bound
	if ub % 2 == 1:
		ub += 1
	if ub <= len(primeL): 
		s = sum(primeL[n] for n in range(ub))
	
		n = ub
		while s < p:
			s += primeL[n] + primeL[n+1]
			n += 2
	
		if s == p:
			ub = n
	else:
		return 0
	
	if ub % 2 == 0:
		ub += 1
	i = 1
	while primeL[i] < (p // ub):
		if ub+i>len(primeL): break
		s = sum(primeL[n] for n in range(i, ub+i))
		n = ub
		while s < p:
			s += primeL[n] + primeL[n+1]
			n += 2
			
		if s == p and n > ub:
			ub = n
			
		i += 1
		
	return ub
		
	

if __name__ == '__main__':
	primeL=[2]
	for n in range(3, 10 ** 6, 2):
		if isprime(n): primeL.append(n)
			
	res = 21
	prime = 941
	for n in primeL:
		if n < 941: continue
		z = maxprimes(n, res)
		if z >= res:
			res = z
			prime = n
			
	print('The prime that can be expressed as the longest consecutive sum of primes\n is %d' % prime)
	