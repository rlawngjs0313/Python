import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int,input().split())
back = []
forward = deque([])
current = 'A'
for _ in range(Q):
    word = list(map(str,input().split()))
    if word[0] == 'B' and len(back) > 0:
        forward.appendleft(current)
        current = back.pop()
    elif word[0] == 'F' and len(forward) > 0:
        back.append(current)
        current = forward.popleft()
    elif word[0] == 'A':
        forward = deque([])
        if current != 'A':
            back.append(current)
        current = word[1]
    elif word[0] == 'C':
        temp = deque([])
        while back:
            if len(temp) == 0:
                temp.appendleft(back.pop())
            else:
                num = back.pop()
                if temp[0] != num:
                    temp.appendleft(num)
        back = list(temp)
print(f"{current}")
if len(back) != 0:
    print(*reversed(back))
else:
    print(-1)
if len(forward) != 0:
    print(*forward)
else:
    print(-1)