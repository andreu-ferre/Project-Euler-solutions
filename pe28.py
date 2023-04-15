nst = input('Please input the size of the matrix ')
n=int(nst)

sum=1
a=1
comdiff=2
for i in range(1, (n+1) // 2):
    for j in range(1,5):
        sum+= (j*comdiff+a)
        if j == 4:
            a+=j*comdiff
    comdiff+=2

print('The sum of diagonals is equal to %d' % sum)
      
