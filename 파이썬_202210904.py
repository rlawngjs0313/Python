from random import randint
from unittest import result

# 6-1
def practice_6_1 ():
    num = map(int, input("정수 5개를 입력하십시오 : ").split())
    return max(num)
# 6-2
def practice_6_2 ():
    A = 0
    B = 0
    trying = int(input("몇 번 던질까요? : "))
    for i in range(0, trying):
        coin = randint(0, 1)
        if coin == 0:
            A += 1
        else:
            B += 1
    print("앞면, 뒷면이 나온 횟수는 각각", A, B, "입니다.")
    print("앞면이 나올 확률은", (A / trying) * 100, "뒷면이 나올 확률은", (B / trying) * 100, "입니다.")

    times = [A, B]
    Prob = [(A / trying) * 100, (B / trying) * 100]
    return times, Prob
# 6-3
def practice_6_3 ():
    num = int(input("1000이하의 숫자를 입력하십시오 : "))
    print(getSumOfDivisors(num))
def getSumOfDivisors (num):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i
    result += num
    return result
# 6-4
def practice_6_4 ():
    print(max(input_1()))
def input_1 ():
    num = []
    num.append(int(input("1000 이하의 정수를 입력하세요 : ")))
    while num.count(1000) != 1:
        num.append(int(input("1000 이하의 정수를 입력하세요 : ")))
    num.remove(1000)
    return num