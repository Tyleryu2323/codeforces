## 1200

from math import sqrt, ceil

def solve():

    n = int(input())
    x = -1
    i = 2
    
    while i < ceil(sqrt(n)):
        if not n % i:
            x = i
            break
        i += 1
    
    if x == -1:
        print(1)
    else:
        print(1 + (n-x)//2)


solve()