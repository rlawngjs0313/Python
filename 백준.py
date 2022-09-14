import sys

n = int(sys.stdin.readline())
queue = [1, ]
cnt = 2

while n-1:
    if cnt % 2 == 0:
        temp = 2
    else:
        temp = 1
    queue.append(sum(queue)+temp)
    n -= 1
    cnt += 1
print(queue.pop() % 10007)