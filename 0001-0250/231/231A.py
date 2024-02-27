## 800

x = int(input())
total = 0
for i in range(x):
    y = input().split()
    if sum([int(j) for j in y]) >= 2:
        total += 1
 
print(total)