def ip(str): return int(input(str))

print("2차 방정식의 해를 구합니다.")
a = ip("a를 입력해주세요: ")
b = ip("b를 입력해주세요: ")
c = ip("c를 입력해주세요: ")

result = b**2 - 4*a*c
if result < 0:
    print("해가 존재하지 않습니다.")
elif result == 0:
    print(f"1개의 해가 존재하며 값은 {(-b + result**(1/2))/(2*a)}입니다. ")
else:
    print(f"2개의 해가 존재하며 값은 {(-b + result**(1/2))/(2*a)}, {(-b - result**(1/2))/(2*a)}입니다. ")