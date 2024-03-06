## 1400

f = open('input.txt', 'r').readlines()
n = int(f[0])
a = []
for i in range(1, n + 1):
    a.append('10'[int(f[i]) % 2])
open('output.txt', 'w').write(' '.join(a))