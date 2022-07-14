N = int(input())
L1 = list(map(int, input().split()))
L1.sort()

def binarySearch(num):
    l = 0
    r = N-1
    while l <= r :
        index = (l+r)//2
        if L1[index] == num :
            return 1
        elif L1[index] > num :
            r = index - 1
        else:
            l = index + 1
    return 0

input()
for i in list(map(int, input().split())):
    print(binarySearch(i), end = ' ')