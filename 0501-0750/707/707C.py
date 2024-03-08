## 1500

def solve():
    
    x = int(input())
    
    
    if x == 1 or x == 2:
        print(-1)
    
    elif x % 2:
        print( (x**2 - 1) // 2, (x**2 + 1) // 2 )
    else:
        print( x**2 // 4 -1, x**2 //4 + 1)
    

if __name__ == "__main__":
    solve()