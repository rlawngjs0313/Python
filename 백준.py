import sys

data = input()
L1 = []
for i in range(len(data)):
    L1.append(data[i:])
L1.sort()
for i in L1:
    sys.stdout.write(str(i) + '\n')