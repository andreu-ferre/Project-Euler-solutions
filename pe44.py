from pe45 import ispentagonal

if __name__ == '__main__':
	res = 5000000000000
	for n in range(1,10000):
		x = (n*(3*n-1)) // 2
		for m in range(n, 10000):
			y = (m*(3*m-1)) // 2
			if ispentagonal(x+y) and x-y != 0 and ispentagonal(y-x):
				if abs(y-x) < res:
					res = abs(y-x)
					
					
	print('The minimum value of D is %d' % res)
	
	# Would ideally need some good justification for the bounds on n and m;
	# as it stands it's a "ballpark issue