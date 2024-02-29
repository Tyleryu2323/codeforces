## 1300

def solve():

    d = int(input())

    if d == 0:
        print("Y", 0, 0)
        return
    if d < 4:
        print("N")
        return

    low = 0 
    high = 1
    mid = (low + high) / 2
    a = d - 1 - mid
    b = 1 + mid

    while abs(d - a * b) > 0.000001:

        if d > a * b:
            low = mid
        else:
            high = mid
        mid = (low + high) / 2
        a = d - 1 - mid
        b = 1 + mid
    
    print("Y", a, b)

    
for _ in range(int(input())):
    solve()