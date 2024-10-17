import sys

queue = []
L1 = []
r,c = map(int, input().split())

for i in range(10):
    temp = []
    for idx,val in enumerate(sys.stdin.readline().rstrip()):
        temp.append(val)
        if val == 'o':
            queue.append((i,idx))
    L1.append(temp)

while queue != []:
    node = queue.pop()
    for i in range(10):
        L1[i][node[1]] = 'o'
    for i in range(10):
        L1[node[0]][i] = 'o'

queue = [(r-1,c-1)]
visited = []
while queue != []:
    node = queue.pop(0)
    if L1[node[0]][node[1]] == 'x':
        print(abs((node[0]+1)-r)+abs((node[1]+1)-c))
        exit()
    else:
        if node not in visited:
            visited.append(node)
            for i in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                if 0<=i[0]<10 and 0<=i[1]<10:
                    queue.append(i)