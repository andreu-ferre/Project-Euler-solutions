import math
def isprime(n):
	if n == 2 or n == 3 or n == 5 or n == 7:
		return True
	if n % 2 == 0:
		return False
	if n % 6 != 1 and n % 6 != 5:
		return False
	for j in range(3, int(math.sqrt(n))+3, 2):
		if n % j == 0:
			return False
	return True

def permutations(seq):
	if not seq:
		return [seq]
	else:
		res = []
		for i in range(len(seq)):
			rest = seq[:i]+seq[i+1:]
			for x in permutations(rest):
				res.append(seq[i:i+1] + x)
		return res
	
		

if __name__ == '__main__':
	L = '1234567'
	R = permutations(L)
	print(R)
	res = 0
	for n in range(len(R)):
		x = int(R[n])
		if isprime(x) and x > res:
			res = x
	print('The largest n-digit pandigital number is %d' % res)
		
	
	
	