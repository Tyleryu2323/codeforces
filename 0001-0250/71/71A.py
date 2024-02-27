## 800

x = int(input())

for i in range(x):
    line = input()
    if len(line) > 10:
        print(line[0] + str(len(line[1:len(line)-1])) + line[-1])
    else:
        print(line)
    