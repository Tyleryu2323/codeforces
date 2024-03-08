## 1500

def solve():
    _ = input()
    s = list(map(int, input().split()))
    count = {}
    m = -1
    for x in s:
        if x not in count:
            count[x] = 1
            m = max(x, m)
        else:
            count[x] += 1
    
    dp = [0] * (m+2)

    for i in range(2, m + 2):
        a = 0
        if i-1 in count:
            a = count[i-1]
            
        dp[i] = max(dp[i-1], a * (i-1) + dp[i-2])
    
    
    print(dp[-1])
    
    
if __name__ == "__main__":
    solve()