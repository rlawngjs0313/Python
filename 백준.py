import sys      # 1517번 버블 소트
sys.setrecursionlimit(1000000)

def mergeSort(start, end):
    global swap, A

    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if A[a] <= A[b]:
                temp.append(A[a])
                a += 1
            else:
                temp.append(A[b])
                b += 1
                swap += (mid - a + 1)

        if a <= mid:
            temp = temp + A[a:mid + 1]
        if b <= end:
            temp = temp + A[b:end + 1]

        for i in range(len(temp)):
            A[start + i] = temp[i]

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
swap = 0
mergeSort(0, N-1)
print(swap)