import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager ,rc

font_path = "C:/Windows/Fonts/ngulim.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

x = np.linspace(0, 2*np.pi, 120)
fx = (np.sin(2*np.pi*x) - np.exp(x)) / np.cos(x)
plt.title('김주헌 그래프', fontsize=15, color='red')
plt.plot(x,fx)
plt.show()