import sys, heapq  #1202번 보석 도둑

N, K = map(int, sys.stdin.readline().split())
Data = []
backpack = []
result = 0

for _ in range(N):  # 힙 정렬 이용해서 시간 줄일 예정
    Data.append(list(map(int, sys.stdin.readline().split())))
for _ in range(K):  # 힙 정렬 이용해서 시간 줄일 예정
    heapq.heappush(backpack, int(sys.stdin.readline()))

# 최대 가격으로 정렬된 보석과 최소 무게로 정렬된 가방
# 비교하면서 최소 무게에 들어갈 수 있으면 넣고 아님 다른 가방 찾기
# 찾는데 없으면 패스

print(result)