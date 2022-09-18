import sys

N = int(sys.stdin.readline())
result = 0
sequenceQueue = []

for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    dataSequence = data.index(min(data))
    dataCost = data[dataSequence]
    if sequenceQueue != []:
        if sequenceQueue.pop() == dataSequence:
            tempData = data[:]
            tempData.pop(dataSequence)
            dataSequence = data.index(min(tempData))
            dataCost = data[dataSequence]
    result += dataCost
    sequenceQueue.append(dataSequence)

print(result)