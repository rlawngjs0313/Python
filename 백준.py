import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
word = "IO"*N + "I"
index = 1
cnt = 0

while True:
    result = S.find(word, index-1)
    if result != -1:
        cnt += 1
        index = result + 3
    else:
        break

print(cnt)