## 1000

def solve():
    s = input()
    
    prevRemoved = False
    
    toRemove = "1"
    
    for i in range(len(s)):
        if s[i] == toRemove and not prevRemoved:
            prevRemoved = True
        
        elif s[i] == toRemove and prevRemoved:
            if toRemove == "0":
                print("NO")
                return
            else:
                toRemove = "0"
                prevRemoved = False
        else:
            prevRemoved = False
            
    print("YES")
        
        
for _ in range(1):
    for i in range(int(input())):
        solve()