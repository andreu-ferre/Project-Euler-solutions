def isbinpal(n):
	l=bin(n)[2:]
	if l == l[::-1]:
		return True
	else:
		return False

sum=0
for i in range(1,10):
	x = i*11
	if isbinpal(x): sum += x
	t = i
	if isbinpal(t): sum += t
	for j in range(10):
		y = i*101+j*10
		if isbinpal(y): sum += y
		
for i in range(1, 10):
	for j in range(10):
		a = i*1001+j*110
		if isbinpal(a): sum += a
		for k in range(10):
			b = i*10001+j*1010+k*100
			if isbinpal(b): sum += b
			c = i*100001+j*10010+k*1100
			if isbinpal(c): sum += c

print('The total sum of doubly palindromic numbers up to a million is %d' % sum)