import math
S=set(j for j in range(0,10))

target = 10 ** 6
res=tuple()
curr = 0

def condition(parity, curr, target):
	if parity == -1:
		return curr<target
	else:
		return curr>target
	
def operation(parity, curr, index):
	if parity == -1:
		curr += math.factorial(index)
		return curr
	else:
		curr -= math.factorial(index)
		return curr
for j in range(9, 0, -1):
	a = 0
	parity = (-1) ** j
	while condition(parity, curr, target):
		curr = operation(parity, curr, j)
		a += 1
	res += (a,)
	parity *= -1

print(res)

	
	


	