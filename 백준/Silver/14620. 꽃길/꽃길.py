import sys
input = sys.stdin.readline
print = sys.stdout.write

def BFS(visited:list,cost,cnt):
    global result
    if cnt == 3:
        result = min(result,cost)
        return 0
    for a in range(1,N-1):
        for b in range(1,N-1):
            x,y = a,b
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if (0<=i<N and 0<=j<N) and not visited[i][j]:
                    continue
                break
            else:
                temp_cost = L1[x][y]+L1[x+1][y]+L1[x-1][y]+L1[x][y+1]+L1[x][y-1]
                visited[x][y],visited[x+1][y],visited[x-1][y],visited[x][y+1],visited[x][y-1] = True,True,True,True,True
                BFS(visited,cost+temp_cost,cnt+1)
                visited[x][y],visited[x+1][y],visited[x-1][y],visited[x][y+1],visited[x][y-1] = False,False,False,False,False


N = int(input())
L1 = []
result = 1e8
for _ in range(N):
    L1.append(list(map(int,input().split())))

vis = [[False for _ in range(N)] for _ in range(N)]
BFS(vis,0,0)
print(f"{result}\n")