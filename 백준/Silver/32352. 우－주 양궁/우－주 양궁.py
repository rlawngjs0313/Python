import sys
input = sys.stdin.readline
print = sys.stdout.write

X1,X2,Y1,Y2,Z1,Z2 = map(int,input().split())
x1,x2,y1,y2,z1,z2 = map(int,input().split())

if (X2 <= x1 or X1 >= x2) or (Y2 <= y1 or Y1 >= y2):
    print('-1\n')
    exit()
else:
    print(f"{min(abs(z2-Z1)+1,abs(Z2-z1)+1)}")