## 1200

from math import lcm
 
n = int(input())
s = list(map(int, input().split()))
 
for i in range(n):
    
    print(lcm(4 *s[i], s[i]+1) // (s[i] + 1) + 1)
    