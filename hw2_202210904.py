import numpy as np
import matplotlib.pyplot as plt

def f(x) :                  #
    if x<=-1 :              #
        return x + 2        # f(x) 설정
    if x>-1 :               #
        return x**2         #

x = np.linspace (-3, 5, 100) # x축 설정
fx = np.zeros_like(x) # (?) y축 설정

for i in range(0,100) :     #
    fx[i] = f(x[i])         # f(x) 계산

plt.plot(x, fx, '.')
plt.show()