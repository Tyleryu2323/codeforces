## 1100

from collections import defaultdict

def solve():

    n, t = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    count0 = defaultdict(int)
    count1 = defaultdict(int)
    l = [-1 for _ in range(n)]

    for i in range(n):
        
        if count0[t - a[i]] < count1[t - a[i]]:
            l[i] = 0
            count0[a[i]] += 1
        else:
            l[i] = 1
            count1[a[i]] += 1
        #print(count0[t - a[i]] > count1[t - a[i]], l, count0, count1)
    
    s = str(l[0])
    for i in range(1, n):
        s += " "
        s += str(l[i])
    
    print(s)

for _ in range(int(input())):
    solve()