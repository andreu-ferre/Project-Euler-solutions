from pe41 import isprime

def istrunc(p):
	x = str(p)
	l = len(x)
	for n in range(1, l):
		s1 = x[n:]
		y = int(s1)
		if y not in primeL:
			return False
			
		s2 = x[:-n]
		z = int(s2)
		if z not in primeL:
			return False
	
	return True
		
	
if __name__ == '__main__':
	primeL = [2]
	for n in range(3, 999999, 2):
		if isprime(n):
			primeL.append(n)
	
	res = 0
	for m in range(len(primeL)):
		if istrunc(primeL[m]) and primeL[m] > 10:
			print(primeL[m])
			res += primeL[m]
			print(res)
	
	
	