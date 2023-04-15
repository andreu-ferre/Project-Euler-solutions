from pe41 import isprime, permutations

def isarithm(a, b, c):
	L = [a, b, c]
	y = (L[2]+L[0]) // 2
	if y == L[1]:
		return True
	else: 
		return False
		
def choice(L):
	res = [[x] for x in L]
	while len(res[0]) < 3:
		temp = []
		for n in range(len(res)):
			for m in range(len(L)):
				if L[m] not in res[n]:
					x = res[n] + [L[m]] 
					temp.append(x)
			
		res = temp
	return res
		
if __name__ == '__main__':
	primeL = []
	for n in range(1001, 9999, 2):
		if isprime(n):
			primeL.append(n)
	
	for x in primeL:
		pool = []
		z = permutations(str(x))
		for n in range(len(z)):
			t = int(z[n])
			if t > 1000 and isprime(t) and t not in pool:
				pool.append(t)
		pool.sort()

		if len(pool) >= 3:
			y = choice(pool)
			for n in range(len(y)):
				if isarithm(y[n][0], y[n][1], y[n][2]):
					print(y[n])
			# To do: do not print permutations of the same set
		
				

