## 1500

parent = [i for i in range(26)]
used = [0] * 26

n = int(input())

for i in range(n):
    s = [ord(c) - 97 for c in input().strip()]
    p = parent[s[0]]
    for q in s:
        used[q] = 1
        parent[parent[q]] = p
        parent[q] = p

total = 0
for i in range(26):
    if parent[i] == i and used[i]:
        total += 1

print(total)