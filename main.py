import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1, label="sin")
plt.plot(x,y2, linestyle="--",label="cos")
plt.legend()
plt.show()
