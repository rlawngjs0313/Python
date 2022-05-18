import sys

A = int(input())
for i in range(0,A):
    B, C = map(int, sys.stdin.readline().split())
    print(B+C)