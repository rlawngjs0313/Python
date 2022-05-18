while True:
    num1 = int(input("첫 번째 숫자를 입력하세요.: "))
    num2 = int(input("두 번째 숫자를 입력하세요.: "))
    symbol = input("기호를 입력하세요.: ")
    if symbol in "+-*/":
        break

if symbol == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif symbol == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif symbol == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    while True:
        if num2 == 0:
            num2 = int(input("두 번째 숫자를 0제외 숫자로 입력하세요.: "))
        else:
            break
    print(f"{num1} / {num2} = {num1 / num2}")