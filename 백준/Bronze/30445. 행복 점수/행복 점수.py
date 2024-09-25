import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

word = input()
Ph, Pg = 0, 0

for i in word:
    if i in "SAD":
        Pg += 1
    if i in "HAPY":
        Ph += 1

if Pg == 0 and Ph == 0:
    print("50.00")
else:
    print(f"{round(decimal.Decimal((Ph/(Ph+Pg))*100),2)}")