## 800

def solve():
    ll = int(input())
    
    a = input()
    b = input()
    c = input()
    
    for i in range(ll):
        if a[i] == b[i] and a[i] != c[i]:
            print("YES")
            return
        if a[i] != c[i] and b[i] != c[i]:
            print("YES")
            return
    print("NO")

for _ in range(int(input())):
    solve()