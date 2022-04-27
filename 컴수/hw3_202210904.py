import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 30, 1000)
y = (np.log2(x) / np.log2(3)) * (np.log2(x) / np.log2(3) - 4) + 3

plt.plot(x, y)
plt.show()