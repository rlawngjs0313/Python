import sympy as sp

x, k = sp.symbols('x k')
fx = sp.exp(2*x)*sp.sin(3*x)

result = sp.solve(sp.diff(fx, x, 2)+k*sp.diff(fx, x)+13*fx)
print(result)