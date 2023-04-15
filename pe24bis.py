import math
L=[i for i in range(10)]
bound = 10 ** 6-1
res=''
for i in range(9,0,-1):
	index = bound // math.factorial(i)
	res += str(L[index])
	bound -= math.factorial(i)*index
	L.pop(index)
	
res += str(L[0])

print(res)
	
	