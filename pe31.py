coins = [1, 2, 5, 10, 20, 50, 100, 200]
goal = 200

coinsrev = coins[::-1]
results = [(1,), (0,)]

def bound(tup):
	l = len(tup)
	res = 200
	for i in range(l):
		res -= tup[i]*coinsrev[i]
	res //= coinsrev[l]
	return res

def tuplegrow(li):
	l = len(li[0])
	res = []
	for n in range(len(li)):
		upper = bound(li[n])
		#print(upper)
		for m in range(upper+1):
			x = li[n]+(m,)
			res.append(x)
			
	return res
	
while len(results[0])<7:
	results = tuplegrow(results)

#print(results)
print('There are %d many ways to produce 200p' % len(results))
			
	
	
	