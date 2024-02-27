## 800

def solve():
    l = int(input())
    s = input()
    
    total = 0
    for i in s:
        if i == "+":
            total += 1
        else:
            total -= 1
    
    print(abs(total))
    
        
for _ in range(1):
    for i in range(int(input())):
        solve()