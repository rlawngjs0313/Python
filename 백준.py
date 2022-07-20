import heapq
import sys

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    visited = [False] * k # 삭제한 값인지 판별하기 위해

    for j in range(k):
        com, num = sys.stdin.readline().split()

        if com == 'I':
            heapq.heappush(min_heap, (int(num), j))
            heapq.heappush(max_heap, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        a = -max_heap[0][0]
        b = min_heap[0][0]
        print(f"{a} {b}")