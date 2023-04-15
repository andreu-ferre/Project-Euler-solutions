from pe41 import permutations

def ispandigital(n):
	res = ()
	for i in range(1, 6):
		x = int(n[:i])
		for j in range(i+1, 8):
			y = int(n[i:j])
			z = int(n[j: 9])
			if x * y == z:
				res += (z,)
	
	if res == ():
		return (False,)
	else:
		return (True,) + res
		

if __name__ == '__main__':
	S = set()
	# What about things like 12345678 * 9?
	L = permutations('123456789')
	for m in L:
		z = ispandigital(m)
		if z[0]:
			for j in range(1, len(z)):
				S = S.union({z[j]})
					
	L = list(S)
	print(L)
	res = 0
	for n in range(len(L)):
		res += L[n]
	
	print('The sum of all pandigital products is equal to %d' % res)
			
			