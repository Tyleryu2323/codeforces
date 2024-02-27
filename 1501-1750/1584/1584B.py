## 1000

from math import ceil
def solve():
    n, m = [int(i) for i in input().split()]
    
    print(ceil(n*m/3))

for _ in range(int(input())):
    solve()