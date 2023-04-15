from pe41 import isprime

if __name__ == '__main__':
	primeL=[2]
	for n in range(3, 10 ** 6, 2):
		if isprime(n): primeL.append(n)
			
	res = 0
	tot = 0
	prime = 2
	for n in primeL:
		tot = 0
		tot += primeL[n]
		counter = 1
		i = n+1
		if i > len(primeL)-res-1: break
		while tot < primeL[-1]:
			tot += primeL[i] + primeL[i+1]
			i += 2
			counter += 2
			if tot in primeL and counter >= res:
				prime = tot
				res = counter
	
	print('The prime that can be expressed as the longest consecutive sum of primes\n is %d' % prime)