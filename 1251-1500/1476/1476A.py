## 1000

def solve():
    n, k = [int(i) for i in input().split()]

    if k < n:
        if n % k:
            print(2)
        else:
            print(1)
        
    else:
        if k % n:
            print( k // n + 1)
        else:
            print( k // n )


for _ in range(int(input())):
    solve()