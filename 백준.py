import sys
# 2668번 숫자 고르기 / 1부터 사이클을 돌면서 N번까지 자기 자신의 수로 안간다면 X, 간다면(순환한다면) set에 추가
N = int(input())
L1 = [0 for _ in range(N+1)]

for i in range(1, N+1):
    L1[i] = int(input())

while True:
    L1[1]