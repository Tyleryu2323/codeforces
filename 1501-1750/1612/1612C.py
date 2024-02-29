## 1300

def solve():

    k, x = map(int, input().split())

    def calval(po):
        
        if po <= k:
            return (1 + po) * po // 2
        else:
            return (1 + k ) * k // 2 + k * (k-1) //2 - (2* k - 1 - po) * (2* k - po) // 2

    l = 1
    r = 2 * k - 1

    while l < r:
        mid = (l+r) // 2 
        if calval(mid) < x:
            l = mid + 1
        else:
            r = mid
    print(r)

for _ in range(int(input())):
    solve()