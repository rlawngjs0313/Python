import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = [0,0,0]
L2 = [0,0,0]

for _ in range(N):
    a,b,c = map(int, input().split())
    temp_L1 = [0,0,0]
    temp_L2 = [0,0,0]
    temp_L1[0] = max(L1[0]+a,L1[1]+a)
    temp_L2[0] = min(L2[0]+a,L2[1]+a)
    temp_L1[1] = max(L1[0]+b,L1[1]+b,L1[2]+b)
    temp_L2[1] = min(L2[0]+b,L2[1]+b,L2[2]+b)
    temp_L1[2] = max(L1[1]+c,L1[2]+c)
    temp_L2[2] = min(L2[1]+c,L2[2]+c)
    L1, L2 = temp_L1, temp_L2

print(f"{max(L1)} {min(L2)}\n")