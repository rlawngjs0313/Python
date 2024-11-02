import sys
from heapq import heappush,heappop
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
heap = []
for _ in range(N):
    word = int(input())
    if word == 0:
        if heap != []:
            print(f"{heappop(heap)[1]}\n")
        else:
            print(f"0\n")
    else:
        heappush(heap,(abs(word),word))