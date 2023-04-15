mult3=0
mult5=0
mult15=0
for i in range(2,1000):
    if i % 3 == 0:
        mult3+=i
    if i % 5 == 0:
        mult5+=i
    if i % 15 == 0:
        mult15+=i

print(mult3+mult5-mult15)
    
