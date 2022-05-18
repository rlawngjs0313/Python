import sympy as sp

x = sp.Symbol('x')
y = sp.Symbol('y')
fx = 1 / x*(x+1)
fy = (2*y-3) / (y**2-3*y+2)
print("F(x) =", sp.integrate(fx, x))
print("F(y) =", sp.integrate(fy, y))