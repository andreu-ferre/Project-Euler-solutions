def nextfirst(tup):
	if tup[1] == 12:
		return (1, 1, tup[2]+1)
	else:
		return (1, tup[1]+1, tup[2])

def isleap(year):
	x = year % 4
	y = year % 400
	if x == 0 and year % 100 == 0:
		if y == 0:
			return True
		else:
			return False
	elif x == 0 and year % 100 != 0:
		return True
	elif not x == 0:
		return False

# Jan 6th 1901 first Sunday of the year
 # it was Tuesday

def issunday(tup):
	days = 0
	start = (1, 1, 1901)
	yeardays = (tup[2] - start[2]) // 4 + 365 * (tup[2] - start[2])
	days += yeardays
	D={1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
	if isleap(tup[2]):
		D[2] = 29
	else:
		D[2] = 28
	monthdays = 0
	if tup[1] != 1: 
		for n in range(1, tup[1]):
			monthdays += D[n]
	days += monthdays
	if days % 7 == 5:
		return True
	else:
		return False
	
res = 0
mangle = (1, 1, 1901)

while mangle[2] <= 2000 and mangle[1] <= 12:
	if issunday(mangle):
		res += 1
	mangle = nextfirst(mangle)
	
print('The number of Sundays for the 20th century is %d' % res)