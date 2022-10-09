import sys


print("삼각형의 세 변의 길이를 입력하세요: ex) 1 2 3")
L1 = list(map(int, sys.stdin.readline().split()))
large = L1.pop(L1.index(max(L1)))
result = L1[0]**2 + L1[1]**2
result2 = large**2
if result > result2:
    print("예각삼각형입니다.")
elif result == result2:
    print("직각삼각형입니다.")
else:
    print("둔각삼각형입니다.")
