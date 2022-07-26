import sys

data = list(map(str, sys.stdin.readline().rstrip()))
L1 = []
result = 0
isLaser = False

for i in range(len(data)):
    if isLaser:
        isLaser = False
        continue
    if data[i] == "(" and data[i+1] == ")":
        result += len(L1)
        isLaser = True
    elif data[i] == "(":
        L1.append(data[i])
    elif data[i] == ")":
        L1.pop()
        result += 1
print(result)