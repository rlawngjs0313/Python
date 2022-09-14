import sys
# F = 9/5C+32
# C = 5/9(F-32)

sys.stdout.write("온도변환" + '\n' + "1. 섭씨 --> 화씨" + '\n' + "2. 화씨 --> 섭씨" + '\n' + "번호를 선택하세요 : ")
n = int(sys.stdin.readline())

if n == 1:
    C = int(input("섭씨 온도를 입력하세요: "))
    F = (9/5)*C+32
    sys.stdout.write(f"섭씨 온도는 {C}도, 화씨 온도는 {F}도입니다.")
elif n == 2:
    F = int(input("화씨 온도를 입력하세요: "))
    C = (5/9)*(F-32)
    sys.stdout.write(f"섭씨 온도는 {C}도, 화씨 온도는 {F}도입니다.")
else:
    sys.stdout.write("잘못 입력하였습니다.")