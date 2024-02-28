## 1100

def solve():
    a, b = input().split()

    print(int(a) * (len(str(int(b)+1)) - 1))


for _ in range(int(input())):
    solve()