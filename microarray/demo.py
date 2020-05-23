import numpy as np

# l = range(100)
# print([i**2 for i in l])

# a = np.arange(100)
# print(a**2)


# c = np.array([[[1], [2]], [[3], [4]]])
# print(c.ndim)
# print(c.shape)


import matplotlib.pyplot as plt

# # 1D plotting:
# x = np.linspace(0, 3, 30)
# y = np.linspace(0, 9, 30)
# plt.plot(x, y)       # line plot    
# plt.plot(x, y, 'o')  # dot plot  
# plt.show()


# 2D arrays (such as images):
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)    
plt.colorbar()  
plt.show()

# slicing
# newslice = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
# plt.imshow(newslice, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()

# excercise
array1 = np.arange(3) + np.arange(1)