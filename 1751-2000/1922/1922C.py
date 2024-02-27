## 1300

x= int(input())
 
for xxx in range(x):
    ll = int(input())
    cities = input().split()
    cities = [int(i) for i in cities]
    
    
    forward = [0] * ll
    backward = [0] * ll
    cur, nextt = cities[1] - cities[0], 0
    forward[1] = 1
    if ll > 2:
        for i in range(1, ll-1):
            nextt = cities[i+1] - cities[i]
            if cur > nextt:
                forward[i+1] = forward[i] + 1
            else:
                forward[i+1] = forward[i] + nextt
            cur = nextt
        cur, prev = 0, cities[-1] - cities[0]
        for i in range(ll-1, 0, -1):
            cur = cities[i] - cities[i-1]
            if prev > cur:
                backward[i-1] = backward[i] + 1
            else:
                backward[i-1] = backward[i] + cur
            prev = cur
    else:
        forward = [0, 1]
        backward = [1, 0]
    
    y = int(input())
    for j in range(y):
        a, b = input().split()
        a, b = int(a), int(b)
        if a < b:
            print(forward[b-1] - forward[a-1] )
        else:
            print(backward[b-1] - backward[a-1])