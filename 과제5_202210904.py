from socket import NI_NUMERICSERV


def readNumber():
    num = int(input("정수 한 개를 입력하세요: "))
    if num <= 1:
        print("2 이상의 숫자를 입력하세요.")
        readNumber()
    else:
        return num
def getDivisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return len(divisors)
def isPrime(num):
    for i in range(2, num+1):
        if num == i:
            return True
        elif num % i == 0:
            return False

number = readNumber()
for i in range(2, number+1):
    divisors = getDivisors(i)
    prime = isPrime(i)
    print(f"정수: {i} 약수 개수: {divisors} 소수: {prime}")