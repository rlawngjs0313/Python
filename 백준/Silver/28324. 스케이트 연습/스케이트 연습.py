import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = list(map(int,input().split()))
result = 0
idx = 0
for i in reversed(L1):
    if i < idx+1:
        idx = i
    else:
        idx += 1
    result += idx

print(f"{result}\n")