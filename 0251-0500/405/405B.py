## 1100

def solve():

    n = int(input())
    s = input()

    opposite = {"L": "R", "R": "L", "": ""}
    cur = ""
    opp = opposite[cur]

    total = 0
    consec = 0

    for c in s:
        if c == ".":
            consec += 1
        if c == "L":
            if cur == "R":
                if consec % 2:
                    total += 1
            consec = 0
            cur = "L"
        if c == "R":
            total += consec 
            consec = 0
            cur = "R"
    
    if cur == "L" or cur == "":
        total += consec
    print(total)

solve()