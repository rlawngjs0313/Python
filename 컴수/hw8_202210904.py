import sympy as sp

x = sp.Symbol('x')
f1x = sp.exp(x)-1
f2x = sp.Abs(sp.sin(x))
f3x = x*sp.sqrt(x**2+2)
f4x = sp.exp(x)*sp.sin(x)
print("The answer is ", sp.integrate(f1x, (x,0,2)))
print("The answer is ", sp.integrate(f2x, (x,-(sp.pi),sp.pi)))
print("The answer is ", sp.integrate(f3x, (x,1,3)))
print("The answer is ", sp.integrate(f4x, (x,0,sp.pi / 2)))