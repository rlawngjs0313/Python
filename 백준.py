from math import factorial


num = str(factorial(int(input())))
cnt = 0

while num.endswith("0"):
    cnt += 1
    num = num.removesuffix("0")
print(cnt)