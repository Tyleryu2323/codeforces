## 1000
from collections import Counter

def solve():

    n, k = [int(i) for i in input().split()]
    c = Counter(input().split())

    if k == 2:
        if c["2"] > 0 or c["4"] > 0 or c["6"] > 0 or c["8"] > 0 or c["10"] > 0:
            print(0)
        else:
            print(1)
        return

    if k == 3:
        if c["3"] > 0 or c["6"] > 0 or c["9"] > 0:
            print(0)
        elif c["2"] > 0 or c["5"] > 0 or c["8"] > 0:
            print(1)
        else:
            print(2)
        return
    
    if k == 4:
        if c["4"] > 0 or c["8"] > 0:
            print(0)
        elif (c["2"] + c["6"] + c["10"]) > 1:
            print(0)

        elif c["3"] > 0 or c["7"] > 0:
            print(1)

        elif (c["2"]+ c["6"]+ c["10"]) == 1:
            if c["5"] > 0 or c["1"] > 0 or c["9"] > 0:
                print(1)
            else:
                print(2)
        elif (c["1"] + c["5"] + c["9"]) > 1:
            print(2)
        else:
            print(3)
        return

    if k == 5:
        if c["5"] > 0 or c["10"] > 0:
            print(0)
        elif c["4"] > 0 or c["9"] > 0:
            print(1)
        elif c["3"] > 0 or c["8"] > 0:
            print(2)
        elif c["2"] > 0 or c["7"] > 0:
            print(3)
        else:
            print(4)
        return
 
for i in range(int(input())):
    solve()