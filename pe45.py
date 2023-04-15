import math

def istriangular(n):
	z = math.sqrt(1+8*n)
	if z-int(z) == 0:
		return True
	else:
		return False

def ispentagonal(n):
	z = math.sqrt(1+24*n)
	if z-int(z) == 0 and int(z) % 3 == 2:
		return True
	else:
		return False

def ishexagonal(n):
	z = math.sqrt(1+8*n)
	if z-int(z) == 0 and int(z) % 4 == 3:
		return True
	else:
		return False

if __name__ == '__main__':

	m = 286
	while not ispentagonal((m*(m+1)) // 2) or not ishexagonal((m*(m+1))//2):
		m += 1
	
	res = (m*(m+1)) // 2
	print('The next triangle number that is also pentagonal and hexagonal is %d' % res)