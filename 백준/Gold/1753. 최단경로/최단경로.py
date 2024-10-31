import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline
print = sys.stdout.write

V, E = map(int, input().split())
K = int(input())
INF = 1e8
graph = defaultdict(list)
dist = [INF for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

queue = []
heappush(queue,(0,K))
dist[K] = 0
while queue:
    node_dist, node = heappop(queue)
    if dist[node] < node_dist:
        continue
    for target, target_dist in graph[node]:
        if node_dist+target_dist < dist[target]:
            dist[target] = node_dist+target_dist
            heappush(queue,(node_dist+target_dist,target))

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF\n')
    else:
        print(f"{dist[i]}\n")