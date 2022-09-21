import sys
from collections import deque

graph = []
queue = deque()
visit = []
for i in range(6):
    graph.append(list(map(int, sys.stdin.readline().split())))

