D={}
for x in range(97,123):
	D[chr(x).upper()]=x-96
	
def value(name):
	res = 0
	for m in range(len(name)):
		res += D[name[m]]
	return res
	
f = open('p022_names.txt')
text = f.read()
L=[x for x in text.split('"') if not x.startswith(',')]
L.pop(0); L.pop(-1)
L.sort()

total = 0
for n in range(len(L)):
	total += (n+1)*value(L[n])
	
print('The total of all the name scores is equal to %d' % total)