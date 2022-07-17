import sys

N1 = [1, 0]
result = [1, 1]
index = [0,0]

N = int(input())
for i in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        sys.stdout.write(f"{N1[0]} {N1[1]}" + "\n")
    elif data == 1:
        sys.stdout.write(f"{N1[1]} {N1[0]}" + "\n")
    else:
        for i in range(data-2):
            result[0], result[1] = result[1], (result[0]+result[1])
        sys.stdout.write(f"{result[0]} {result[1]}" + "\n")
    result = [1, 1]