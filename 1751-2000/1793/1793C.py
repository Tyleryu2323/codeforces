## 1200

def solve():
    ma = int(input())
    mi = 1
    perm = [int(x) for x in input().split()]
    l = 0
    r = ma - 1
    
    while l <= r:
        
        if perm[l] == mi:
            l += 1
            mi += 1
        elif perm[l] == ma:
            l += 1
            ma -= 1
        elif perm[r] == mi:
            r -= 1
            mi += 1
        elif perm[r] == ma:
            r -= 1
            ma -= 1
        else:
            break
        
    if l <= r:
        print(l+1, r+1)
        return
    else:
        print(-1)
        return
        
for _ in range(1):
    for i in range(int(input())):
        solve()