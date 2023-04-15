import math

def istriangle(number):
    fp = math.sqrt(1+8*number)-int(math.sqrt(1+8*number))
    if fp == 0: 
        return True
    else:
        return False

D={'A':1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}
f=open('p042_words.txt')
text=f.read()
L=[x for x in text.split('"') if not x.startswith(',')]
L.pop(0); L.pop(-1)
counter=0
for x in L:
    wordvalue=sum(D[x[i]] for i in range(len(x)))
    if istriangle(wordvalue): counter+=1

print('The total number of triangle words is %d' % counter)
        
    
    
