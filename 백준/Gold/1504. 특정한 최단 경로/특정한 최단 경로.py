import sys
from collections import defaultdict
from heapq import heappop,heappush
input = sys.stdin.readline
print = sys.stdout.write

N, E = map(int,input().split())
graph = defaultdict(list)
INF = 1e8

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2 = map(int,input().split())

def solution(n):
    heap = []
    heappush(heap,(0,n))
    dist = [INF for _ in range(N+1)]
    dist[n] = 0
    while heap:
        node_dist,node = heappop(heap)
        if dist[node]<node_dist:
            continue
        for target_dist,target in graph[node]:
            if node_dist+target_dist < dist[target]:
                dist[target] = node_dist+target_dist
                heappush(heap,(node_dist+target_dist,target))
    return dist

result = INF
result = min(solution(1)[v1]+solution(v1)[v2]+solution(v2)[N], solution(1)[v2]+solution(v2)[v1]+solution(v1)[N])

if result < INF:
    print(f"{result}\n")
else:
    print("-1\n")