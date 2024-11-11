import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
L1 = [list(map(int,input().split())) for _ in range(N)]
if L1[N-1][N-1] == 1:
    print('0\n')
    exit()
result = 0
queue = [(0,0,0,1,1)]


#가로:1 세로:2 대각선:3
while queue:
    x1,y1,x2,y2,state = queue.pop()
    if x2 == N-1 and y2 == N-1:
        result += 1
    if state == 1:
        for a,b,c,d,s in [(x2,y2,x2,y2+1,1),(x2,y2,x2+1,y2+1,3)]:
            if (a<N and b<N and c<N and d<N):
                for i in range(a,c+1):
                    if 1 in L1[i][b:d+1]:
                        break
                else:
                    queue.append((a,b,c,d,s))
    elif state == 2:
        for a,b,c,d,s in [(x2,y2,x2+1,y2,2),(x2,y2,x2+1,y2+1,3)]:
            if (a<N and b<N and c<N and d<N):
                for i in range(a,c+1):
                    if 1 in L1[i][b:d+1]:
                        break
                else:
                    queue.append((a,b,c,d,s))
    else:
        for a,b,c,d,s in [(x2,y2,x2,y2+1,1),(x2,y2,x2+1,y2,2),(x2,y2,x2+1,y2+1,3)]:
            if (a<N and b<N and c<N and d<N):
                for i in range(a,c+1):
                    if 1 in L1[i][b:d+1]:
                        break
                else:
                    queue.append((a,b,c,d,s))

print(f"{result}\n")