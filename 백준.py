import sys

N, M = map(int, input().split())
S1 = set()
S2 = set()
for i in range(N):
    S1.add(sys.stdin.readline().rstrip())
for i in range(M):
    S2.add(sys.stdin.readline().rstrip())
print(len(S1.intersection(S2)))
result = sorted(S1.intersection(S2))
for i in result:
    sys.stdout.write(f"{i}" + "\n")