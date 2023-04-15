from pe21 import divsum

bound = 28123

def isabundant(n):
	if divsum(n)>n:
		return True
	else:
		return False

abundant = []
for n in range(2, bound+1):
	if isabundant(n): 
		abundant.append(n)
T = set(abundant)
res = 0
for i in range(1, bound+1):
	S = set([-abundant[n]+i for n in range(len(abundant))])
	x = S.intersection(T)
	if x == set(): 
		res += i

print('The total number of positive integers that cannot be written as a sum',
'of two abundant numbers is %d' % res)
	

	
