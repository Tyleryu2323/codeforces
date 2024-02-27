## 900

def solve():
    n, f, a, b = [ int(i) for i in input().split() ]
    s = [ int(i) for i in input().split() ]
    cur = 0
    
    for nxt in s:
        if (nxt - cur) * a > b:
            f -= b
            n -= 1
        else:
            f -= (nxt - cur) * a
            n -= 1

        if n == 0 and f > 0:
            print("YES")
            return
        
        if f <= 0:
            print("NO")
            return 
        cur = nxt
        
for _ in range(1):
    for i in range(int(input())):
        solve()