## 1400

from math import ceil

def solve():

    k, x, a = map(int, input().split())

    cur = 1

    for i in range(x):
        cur += cur // (k-1) + 1
        if cur > a:
            print("NO")
            return
    
    print("YES")


for _ in range(int(input())):
    solve()
