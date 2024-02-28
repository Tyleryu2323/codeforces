## 1100

from math import floor, sqrt

def solve():

    k = int(input())
    s = floor(sqrt(k))
    a, b = -1, -1
    mods = {0: "aeiou", 1: "eioua", 2: "iouae", 3: "ouaei", 4: "uaeio"}
    for i in range(5, s+1):
        if k % i == 0:
            if k // i > 4:
                a, b = i, k // i 
            else:
                print("-1")
                return
    if a == -1:
        print("-1")
        return

    st = ""
    for i in range(a):
        cur = ""
        while len(cur) < b:
            cur += mods[i % 5]
        st += cur[:b]

    print(st)

solve()