import sys
input = sys.stdin.readline
print = sys.stdout.write

A,B,C,D,E = map(int, input().split())
result = 0

result += E

temp = min(D,A)
D,A,result = D-temp,A-temp,result+temp
result += D

temp = min(C,B)
C,B,result = C-temp,B-temp,result+temp
temp = min(C,A//2)
C,A,result = C-temp,A-temp*2,result+temp
temp = min(C,A)
C,A,result = C-temp,A-temp,result+temp
result += C

temp = min(B//2,A)
B,A,result = B-temp*2,A-temp,result+temp
temp = min(B,A//3)
B,A,result = B-temp,A-temp*3,result+temp
temp = min(B,A//2)
B,A,result = B-temp,A-temp*2,result+temp
result += B//2
B %= 2
temp = min(B,A)
B,A,result = B-temp,A-temp,result+temp
result += B

for i in range(5,0,-1):
    result += A//i
    A %= i

print(f"{result}")