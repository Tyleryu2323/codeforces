## 1400

def solve():
    n, v = map(int, input().split())

    lut = dict(zip(range(1, 3002), [0] * 3001))

    for _ in range(n):
        a, b = map(int, input().split())
        lut[a] += b

    total = 0
    cur = 0

    for d in range(1, 3002):

        if lut[d] + cur > v:
            total += v
            cur = lut[d] - max(v - cur, 0)

        else:
            total += lut[d] + cur
            cur = 0
    
    print(total)

solve()