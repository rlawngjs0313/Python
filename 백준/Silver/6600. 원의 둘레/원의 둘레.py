import sys
import decimal
input = sys.stdin.readline
print = sys.stdout.write
Decimal = decimal.Decimal

pi = Decimal(3.141592653589793)
while True:
    try:
        x1,y1,x2,y2,x3,y3 = map(Decimal,input().split())
        D = 2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        x = 1/D*((x1**2+y1**2)*(y2-y3)+(x2**2+y2**2)*(y3-y1)+(x3**2+y3**2)*(y1-y2))
        y = 1/D*((x1**2+y1**2)*(x3-x2)+(x2**2+y2**2)*(x1-x3)+(x3**2+y3**2)*(x2-x1))
        r = ((x1-x)**2+(y1-y)**2)**Decimal(0.5)
        print(f"{Decimal(2*pi*r).quantize(Decimal('1.00'))}\n")
    except:
        exit()