import time
import sys

n = int(sys.stdin.readline())
start = time.time()
s = n*(n+1)//2
end = time.time()
sys.stdout.write(f"{s} {end-start} 2\n")

start = time.time()
s = 0
for i in range(1, n+1):
    s += i
end = time.time()
sys.stdout.write(f"{s} {end-start} 1 \n")