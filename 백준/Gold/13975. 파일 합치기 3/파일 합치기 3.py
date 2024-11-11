import sys
from heapq import heappop,heappush
input = sys.stdin.readline
print = sys.stdout.write
 
T = int(input())

for _ in range(T):
    K = int(input())
    heap = []
    result = 0
    for i in list(map(int,input().split())):
        heappush(heap,i)
    while len(heap) > 1:
        A,B = heappop(heap),heappop(heap)
        heappush(heap,A+B)
        result += A+B
    print(f"{result}\n")