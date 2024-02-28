## 1100

def solve():
    _ = input()
    s = input()
    
    numT, numM = 0, 0
    for c in s:
        if c == "T":
            numT += 1
        else:
            numM += 1
            numT -= 1
        if numT < 0:
            print("NO")
            return
    
    if numT != numM:
        print("NO")
        return

    numT, numM = 0, 0
    for c in s[::-1]:
        if c == "T":
            numT += 1
        else:
            numM += 1
            numT -= 1
        if numT < 0:
            print("NO")
            return
    
    if numT != numM:
        print("NO")
        return

    
    print("YES")
    


for _ in range(int(input())):
    solve()