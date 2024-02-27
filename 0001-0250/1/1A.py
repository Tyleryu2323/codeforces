## 1000

def solve():
    n, m, a = [int(i) for i in input().split()]
    x = n // a + 1
    y = m // a + 1
    if not n % a:
        x = n // a
    if not m % a:
        y = m // a

    print(x * y)

solve()