## 800

def solve():
    ll = int(input())
    
    s = input()
    
    nL = 0
    nO = 0
    
    for i in range(ll):
        if s[i] == "L":
            nL += 1
        else:
            nO += 1
    
    nnL = 0
    nnO = 0
    for i in range(ll):
        if s[i] == "L":
            nnL += 1
            if nnL != nL - nnL and nnO != nO - nnO and not (nnL == nL and nnO == nO) and nnO + nnL > 0:
                print(i+1)
                return
        else:
            nnO += 1
            if nnL != nL - nnL and nnO != nO - nnO and not (nnL == nL and nnO == nO) and nnO + nnL > 0:
                print(i+1)
                return
    print(-1)
        
        
for _ in range(1):
    solve()