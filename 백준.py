import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
sortedA = []
lastNum = 0

for i in A:
    if i > lastNum:
        sortedA.append(i)
        lastNum = i
    else:
        start = 0
        end = len(sortedA)-1
        while start <= end:
            mid = (end + start) // 2
            if i == sortedA[mid]:
                break
            elif i > sortedA[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if i <= sortedA[mid]:
            sortedA[mid] = i
        else:
            sortedA[mid+1] = i
        lastNum = sortedA[-1]
print(len(sortedA))