digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tenths = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
second = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hun = 'hundred'
word = 'and'
thous = 11
L=[]
L += digits; L += tenths
for n in range(len(second)):
	L.append(second[n])
	for m in range(len(digits)):
		L.append(second[n]+digits[m])
		
for n in range(len(digits)):
	L.append(digits[n]+hun)
	for m in range(len(digits)):
		L.append(digits[n]+hun+word+digits[m])
	for k in range(len(tenths)):
		L.append(digits[n]+hun+word+tenths[k])
	for t in range(len(second)):
		L.append(digits[n]+hun+word+second[t])
		for s in range(len(digits)):
			L.append(digits[n]+hun+word+second[t]+digits[s])
			
sum = 0
for i in range(len(L)):
	sum += len(L[i])
	
sum += thous

print('The total sum is equal to %d' % sum)
	