def count(length, width): 
	res = length*(length+1)*width*(width+1)/4
	return res
	
area = 0
bound = 2 * (10 ** 6)
distance = bound
for n in range(2001):
	for m in range(2001):
		x = abs(count(n,m)-bound)
		if x < distance:
			area = n*m
			distance = x

print('The area is equal to %d' % area)