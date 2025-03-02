import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

L1 = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
if L1[r][c] == 1:
    print(f"0\n")
    exit()
L1[r][c] = -1

queue = deque([(r,c,0)])

while queue:
    a,b,c = queue.popleft()
    for i,j in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
        if (0<=i<5 and 0<=j<5) and L1[i][j] != -1:
            if L1[i][j] == 1:
                print(f"{c+1}\n")
                exit()
            else:
                L1[i][j] = -1
                queue.append((i,j,c+1))

print(f"-1\n")