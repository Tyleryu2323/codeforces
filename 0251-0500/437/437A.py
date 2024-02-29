## 1300

def solve():

    A = input()[2:]
    B = input()[2:]
    C = input()[2:]
    D = input()[2:]
    l = [A, B, C, D]
    ll = ["A", "B", "C", "D"]
    lut = dict(zip(ll, l))
    ll.sort(key=lambda x: len(lut.get(x, [])))
    
    great = []
    if len(lut[ll[0]]) * 2 <= len(lut[ll[1]]):
        great.append(ll[0])
    if len(lut[ll[-2]]) * 2 <= len(lut[ll[-1]]):
        great.append(ll[-1])
    
    if len(great) == 1:
        print(great[0])
    else:
        print("C")


solve()