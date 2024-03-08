## 1500

def solve():
    s = input().strip()
    t = input().strip()
    
    ps = len(s) - 1
    pt = len(t) - 1
    
    while ps >= 0  and pt >= 0:
        
        if s[ps] == t[pt]:
            ps -= 1
            pt -= 1
        else:
            ps -= 2
            
    if pt == -1:
        print("YES")
    else:
        print("NO")
    

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()