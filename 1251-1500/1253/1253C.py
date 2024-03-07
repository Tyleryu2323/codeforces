## 1500

def main():

    n, m = map(int, input().split())

    candy = map(int, input().split())

    candy.sorted()

    ans = []
    cur = 0

    for k in range(n):
        cur += candy[k]
        ans[k] = cur

        if k >= m:
            ans[k] += ans[k - m]
    
    print(' '.join(ans))



if __name__ == "__main__":
    main()