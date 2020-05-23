# text file ko load karna - https://scipy-lectures.org/intro/numpy/advanced_operations.html#polynomials

import numpy as np
import matplotlib.pyplot as plt

# # show noraml rangd uniform data range
data = np.loadtxt('microarray/data/populations.txt')
year, hares, lynxes, carrots = data.T

plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))

# show real plot
# x, y = np.loadtxt('microarray/data/GDS5037.txt', unpack=True)
# plt.plot(x,y, label='Load form file!')
# plt.xlabel(x)
# plt.ylabel(y)
# plt.legend()

# with open('microarray/data/GDS5037.txt') as f:
#     lines = f.readlines()
#     x = [line.split[0] for line in lines]
#     y = [line.split[1] for line in lines]

# print(x)
# print(y)

plt.show()