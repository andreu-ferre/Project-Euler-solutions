import math
def isprime(n):
	if n == 2 or n == 3 or n == 5 or n == 7:
		return True
	if n % 2 == 0:
		return False
    if n % 6 != 1 and n % 6 != -1:
        return False
	for j in range(3, int(math.sqrt(n))+3,2):
		if n % j == 0:
			return False
	return True
	
primeL = []
for n in range(2, 10 ** 6):
	if isprime(n):
		primeL.append(n)

def iscircular(p):
	if p < 10:
		return True
	s = str(p)
	for n in range(len(s)-1):
		y = s[1:]+s[0]
		x = int(y)
		if x not in primeL:
			return False
		s = y
	return True

if __name__ == '__main__':
	print(iscircular(19937))
	res = 0
	#for n in range(0, 25):
	#	if iscircular(primeL[n]):
	#		res += 1
	#print(res)
	for n in range(len(primeL)):
		if iscircular(primeL[n]):
			res += 1
		
	print('There are %d circular primes' % res)
	
		
