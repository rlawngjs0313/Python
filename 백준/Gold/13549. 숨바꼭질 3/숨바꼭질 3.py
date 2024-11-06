import sys
from heapq import heappop, heappush
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
heap = [(0,N)]
visited = {}
if N == K:
    print(f"0\n")
    exit()

visited[N] = 0
while heap:
    cnt, node = heappop(heap)
    if node == K:
        print(f"{cnt}\n")
        exit()
    for c,n in [(cnt+1,node-1),(cnt+1,node+1),(cnt,2*node)]:
        if 0<=n<=100001 and (n not in visited or c < visited[n]):
            heappush(heap,(c,n))
            visited[n] = c