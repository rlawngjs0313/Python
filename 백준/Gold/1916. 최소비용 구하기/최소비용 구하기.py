import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
INF = 1e8
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())
dist = [INF for _ in range(n+1)]

queue = []
heappush(queue,(0,start))
while queue:
    node_dist, node = heappop(queue)
    if dist[node] < node_dist:
        continue
    
    for target, target_dist in graph[node]:
        if target_dist+node_dist < dist[target]:
            dist[target] = target_dist+node_dist
            heappush(queue,(target_dist+node_dist,target))

print(f"{dist[end]}\n")