def factorial(n):
	if n == 1:
		return n
	else:
		return n*factorial(n-1)
		
def dyckpaths(num):
	res = factorial(2*num)/(factorial(num) ** 2)
	return res

number = int(input('What is the size of your grid?\n'))
print('The number of paths in a %dx%d grid is %d' % (number, number, dyckpaths(number)))