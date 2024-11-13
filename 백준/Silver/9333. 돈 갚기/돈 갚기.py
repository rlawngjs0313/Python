import sys
input = sys.stdin.readline
print = sys.stdout.write
import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
Decimal = decimal.Decimal

T = int(input())
for _ in range(T):
    result = 1
    R,B,M = map(Decimal,input().split())
    tax = B*(R/Decimal(100))
    if M <= Decimal(tax).quantize(Decimal('0.01')):
        print("impossible\n")
        continue
    for _ in range(1200):
        A = B*(R/Decimal(100))
        A = Decimal(A).quantize(Decimal('0.01'))
        B = B+A-M
        if B <= Decimal(0):
            print(f"{result}\n")
            break
        result += 1
    else:
        print("impossible\n")