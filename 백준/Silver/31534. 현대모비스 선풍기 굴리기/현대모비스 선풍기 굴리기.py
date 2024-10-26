import math

a, b, h = map(int, input().split())
if a == b:
    print(-1)
    exit()

if a == 0:
    print(f"{(b**2+h**2)*math.pi:0.7f}")
    exit()
elif a > b:
    a, b = b, a

x = b*h/(b-a)
l_large, l_small = x**2+b**2, (x-h)**2+a**2
print(f"{(l_large-l_small)*math.pi:0.7f}")