import matplotlib.pyplot as plt
import numpy as np

data_x = np.arange(0, 50, 2)
data_y = np.arange(0, 50, 3)

[X, Y] = np.meshgrid(data_x, data_y)

fig, ax = plt.subplots(1, 1)

Z = np.cos(X / 2) + np.sin(Y / 4)

ax.contour(X, Y, Z)

ax.set_title('title here')
ax.set_xlabel('x-axis label')
ax.set_ylabel('y-axis label')
plt.index()
plt.show()

