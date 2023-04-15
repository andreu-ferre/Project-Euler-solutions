total=0
partial=0
for i in range(10, 360000):
    s=str(i)
    for j in range(len(s)):
        partial += ((int(s[j])) ** 5)
    if partial == i: total+=i
    partial=0

print('The sum of the numbers that can be written as the sum of fifth powers of'+
'their digits is %d' % total)


    
