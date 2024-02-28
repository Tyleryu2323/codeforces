## 1200

a, b = map(int, input().split())
c, d = map(int, input().split())

l1 = [b + a * i for i in range(100)]
l2 = [d + c * i for i in range(100)]

ans = -1

for i in l1:
    if i in l2:
        ans = i
        break

print(ans)