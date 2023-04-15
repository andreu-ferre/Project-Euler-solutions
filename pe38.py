def result(n):
	x = str(n)
	j = 2
	while len(x) < 10:
		x += str(n * j)
		last = str(n * j)
		j += 1
		
	res = int(x[:len(x)-len(last)])
	return res
	
def length(n):
	z = str(n)
	if len(z) == 9:
		return True
	else:
		return False
		
def ispandigital(n):
	S = set(str(n))
	if S == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
		return True
	else:
		return False

if __name__ == '__main__':
	res = 0
	for n in range(10000):
		y = result(n)
		if length(y) and ispandigital(y) and y > res:
			res = y
			
	print('The largest number is %d' % res)
		
		