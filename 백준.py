import sys

N = int(input())
L1 = list(range(1, N+1))
L2 = []
result = []
index = 0

for i in range(N):
    data = int(sys.stdin.readline())
    if L2 == []:
        while True:
            L2.append(L1.pop(0))
            result.append("+")
            if L2[-1] == data:
                index = L2.pop()
                result.append("-")
                break
    elif L2[-1] <= data:
        while L2[-1] != data:
            L2.append(L1.pop(0))
            result.append("+")
        index = L2.pop()
        result.append("-")
    elif L2[-1] > data:
        result.clear()
        result.append("NO")
        for j in range(N-i-1):
            sys.stdin.readline()
        break
for i in result:
    sys.stdout.write(i + "\n")