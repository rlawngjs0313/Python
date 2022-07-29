import sys

N = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip()
L1 = []
L2 = []
for i in range(N):
    L2.append(float(sys.stdin.readline()))

for i in data:
    if i == "*":
        A = float(L1.pop())
        B = float(L1.pop())
        L1.append(B*A)
    elif i == "/":
        A = float(L1.pop())
        B = float(L1.pop())
        L1.append(B/A)
    elif i == "+":
        A = float(L1.pop())
        B = float(L1.pop())
        L1.append(B+A)
    elif i == "-":
        A = float(L1.pop())
        B = float(L1.pop())
        L1.append(B-A)
    else:
        L1.append(L2[ord(i)-ord("A")])

print(f"{L1[0]:0.2f}")