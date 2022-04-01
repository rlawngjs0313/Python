P = float(input("예치금을 입력하십시오. : "))
T = int(input("예치 기간을 입력하십시오. : "))
R = 0.03
A1 = 0.0
A = P * (1 + R)**T
print(T, "년 후 총 금액은", A, "입니다.")

for i in range(1, T+1) :
    A1 += P * (1 + R)**i
print(T, "년동안 모인 총 금액은", A1, "입니다.")