## 1300

from math import sqrt
x= int(input())
nmlist = []
primes = []
lut = [True] * (10001)
for i in range(2, 10001):
    if lut[i]:
        sq = i*i
        a = 0
        while sq + a*i < 10000:
            lut[sq+a*i] = False
            a += 1
        primes.append(i)
        
def leastdivisor(x):
    for i in primes:
        if i > sqrt(x):
            break
        if not x % i:
            return i
    return -1
    
for i in range(x):
    n, m = input().split()
    n, m = int(n), int(m)
    if n == 1:
        print("YES")
    elif n <= m:
        print("NO")
    else:
        d = leastdivisor(n)
        if d > 0 and d <= m:
            print("NO")
        else:
            print("YES")
 