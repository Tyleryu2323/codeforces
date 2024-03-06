## 1400 

def solve():
    s = input()

    p0 = 1
    p1 = 1
    mod = 10 ** 9 + 7
    if s[0] == "w" or s[0] == "m":
            print(0)
            return
    for i in range(1, len(s)):

        if s[i] == "w" or s[i] == "m":
            print(0)
            return
        if (s[i] == "n" or s[i] == "u") and s[i] == s[i-1]:
            p1, p0 = p1 + p0, p1

        else:
            p0 = p1
    
    print(p1 % mod)


solve()

