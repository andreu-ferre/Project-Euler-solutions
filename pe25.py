fib1=1
fib2=1
n=1
index=2
while len(str(n))<1000:
    n+=fib1
    fib1=fib2
    fib2=n
    index+=1

print('The index of the first Fibonacci number with over 1000 digits is %d' % index)


     
