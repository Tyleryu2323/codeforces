## 900
 
def calc(s):
    total = 0
    l, r = 0, 0
 
    while l < len(s) and s[l] == "B":
        l += 1
        r += 1
    
    while r < len(s):
 
        while r < len(s) and s[r] == "A":
            r += 1
        while r < len(s) and s[r] == "B":
            r += 1
        if s[r-1] == "B":
            total += r - l - 1
            l = r-1
        else: 
            break
        
    return total
 
for i in range(int(input())):
    _ = input()
    s = input()
    
    print(calc(s))
 
