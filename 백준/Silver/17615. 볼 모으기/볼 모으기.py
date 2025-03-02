import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
word = input().rstrip()
result = 10e8

for i in ['R','B']:
    temp = word.rstrip(i)
    result = min(result,temp.count(i))

for i in ['R','B']:
    temp = word.lstrip(i)
    result = min(result,temp.count(i))

print(f"{result}\n")