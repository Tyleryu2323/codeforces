## 1100

def match(A, B):
 
    A.sort()
    B.sort(reverse=True)
    C = B[len(B) - len(A)::]
    s = sum( abs(A[i] - C[i]) for i in range(len(A)))
 
    total = 0
    
    for i in range(len(A)):
        total = max(total, s)
        s -= abs(C[i] - A[i])
        C[i] = B[i]
        s += abs(C[i] - A[i])
        
    return max(total, s)
    
 
for i in range(int(input())):
    _ = input()
    l1 = [int(a) for a in input().split()]
    l2 = [int(a) for a in input().split()]
    l = match(l1, l2)
    
    print(l)