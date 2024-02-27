## 900

from collections import Counter
 
for i in range(int(input())):
    k = int(input().split()[1])
    c = Counter(input())
    
    numodd = len([a for a in c.values() if a % 2])
    
    if k < numodd -1:
        print("NO")
    
    else:
        print("YES")