from itertools import combinations_with_replacement
import time

start = time.time()

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for (a,b,c,d,e,f) in combinations_with_replacement(alphabets, 6):
    print(a+b+c+d+e+f)

end = time.time()
print(end - start)
