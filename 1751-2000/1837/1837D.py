## 1400

for i in range(int(input())):
    _ = input()
    s = input()
    bb = s[0]
    dd = ")" if bb == "(" else "("
    out = []
    nd, nb = 0, 0
    
    for c in s:
        if c == bb and nd > 0:
            out.append("2")
            nd -= 1
        elif c == bb and nd == 0:
            out.append("1")
            nb += 1
        elif c == dd and nb > 0:
            out.append("1")
            nb -= 1
        elif c == dd and nb == 0:
            out.append("2")
            nd += 1
    
    if nd != 0 or nb != 0:
        print(-1)
    else:
        print(max(out))
        print(" ".join(out))