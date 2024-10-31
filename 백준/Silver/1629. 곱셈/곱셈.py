import sys
input = sys.stdin.readline
print = sys.stdout.write

A, B, C = map(int, input().split())
print(f"{pow(A,B,C)}")