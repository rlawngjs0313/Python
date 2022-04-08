import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2, 6, 401)
fx = np.zeros_like(x)

for i in range(0, 401):
    if np.abs(x[i]) < 1:
        fx[i] = 0
    elif x[i] == 1:
        fx[i] = 0.5
    elif x[i] == -1:
        fx[i] = -0.5
    else:
        fx[i] = x[i]

plt.plot(x, fx, '.')
plt.show()