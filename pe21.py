primeL = [2]
c = primeL[0]
d = 1
bound = 3100
while len(primeL) < bound:
	for i in range(c+1, 2*c+2):
		for j in primeL:
			if i % j == 0:
				d = j
				break
		if d == 1:
			primeL.append(i)
			c = i
		else:
			d = 1
		if len(primeL) == bound: break
		
def divprocess(li):
	res = []
	k = len(li)
	copy = li[:]
	for i in range(copy[0][1]+1):
		res.append((copy[0][0] ** i,))
	
	def tuplegrow(givenli, pos):	
		resul = []
		for i in range(len(givenli)):
			for j in range(copy[pos][1]+1):
				tup = givenli[i]+(copy[pos][0] ** j,)
				resul.append(tup)
		return resul
		
	while len(res[0]) < k:
		res = tuplegrow(res, len(res[0]))
	
	prod = 1
	for n in range(len(res)):
		for m in range(k):
			prod *= res[n][m]
		res[n] = prod
		prod = 1

	return res			
	
def divisors(n):
	i = 0
	a = 0
	li = []
	while primeL[i] <= n:
		while n % primeL[i] == 0:
			a += 1
			n //= primeL[i]
		if a > 0:
			li += [[primeL[i], a]]
		i += 1
		a = 0
	#print(li)
	return divprocess(li)

#proper divisors here
def divsum(n):
	l = divisors(n)
	l.remove(n)
	res = 0
	for i in range(len(l)):
		res += l[i]
	return res

totsum = 0
for i in range(2, 10000):
	x = divsum(i)
	if x>1 and divsum(divsum(i)) == i and i != divsum(i):
		totsum += i
		#print(i)

print('The total sum of amicable numbers below 10000 is %d' % totsum)
	
	
		
