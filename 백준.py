import sys
import copy
sys.setrecursionlimit(1000000)

N, M, V = map(int, input().split())
graph_DFS = [[] for _ in range(N+1)]
graph_BFS = []
result_DFS = [V, ]
result_BFS = [V, ]
temp = []

def DFS(node):
    if len(result_DFS) == N:
        return
    if graph_DFS[node] == []:
        return
    for i in range(len(graph_DFS[node])):
        N1 = min(graph_DFS[node])
        graph_DFS[node].remove(N1)
        if N1 in result_DFS:
            continue
        result_DFS.append(N1)
        DFS(N1)

def BFS(node):
    if len(result_BFS) == N:
        return
    if graph_BFS[node] == []:
        return
    for i in range(len(graph_BFS[node])):
        N1 = min(graph_BFS[node])
        graph_BFS[node].remove(N1)
        if N1 in result_BFS:
            continue
        result_BFS.append(N1)
        temp.append(N1)
    
    for i in range(len(temp)):
        if temp:
            BFS(temp.pop(0))
    

for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))
    graph_DFS[data[0]].append(data[1])
    graph_DFS[data[1]].append(data[0])

graph_BFS = copy.deepcopy(graph_DFS)
DFS(V)
result_DFS = str(result_DFS).replace('[', '').replace(']', '').replace(',', '')
BFS(V)
result_BFS = str(result_BFS).replace('[', '').replace(']', '').replace(',', '')
print(result_DFS)
print(result_BFS)