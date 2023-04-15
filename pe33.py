def cancel(n, m):
	x = str(n)
	y = str(m)
	z = n / m
	a = x[0]
	b = x[1]
	c = y[0]
	d = y[1]
	if int(x[0]) == int(y[0]) and int(y[1]) != 0:
		if int(x[1])/int(y[1]) == z:
			return (True, b+'/'+d)
	if int(x[0]) == int(y[1]):
		if int(x[1])/int(y[0]) == z:
			return (True, b+'/'+c)
	if int(x[1]) == int(y[0]) and int(y[1]) != 0:
		if int(x[0]) / int(y[1]) == z:
			return (True, a+'/'+d)
	if int(x[1]) == int(y[1]) and int(x[1]) != 0:
		if int(x[0]) / int(y[0]) == z:
			return (True, a+'/'+c)
	
	return (False,)


if __name__ == '__main__':
	for i in range(10, 100):
		for j in range(10, 100):
			if cancel(i, j)[0] and j > i:
				print('The fraction %d/%d is equal to %s' % (i, j, cancel(i, j)[1]))

			