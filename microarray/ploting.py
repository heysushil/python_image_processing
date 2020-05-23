import numpy as np
import matplotlib.pyplot as plt

# fetch the image
img = plt.imread('microarray/data/gdsDraw.png')
# get the shape and dtype of the iamge
img.shape, img.dtype
# print(img.shape,img.dtype)
# create raw file
# img.tofile('microarray/data/img.raw')
# img_from_raw = np.fromfile('microarray/data/img.raw',dtype=np.float32)

# print(img_from_raw)
# img_from_raw.shape(336420,)
# newimage = img_from_raw.shape(84, 1335, 3)

plt.figure(figsize=(12.5, 3))
# plt.subplot(111)
plt.imshow(img, interpolation='nearest', cmap=plt.cm.nipy_spectral)
# plt.axis('off')
plt.show()
'''Need to know the shape and dtype of the image (how to separate data bytes).
For large data, use np.memmap for memory mapping:'''
# img_memmap = np.memmap('microarray/data/img.raw', dtype=np.float32, shape=(84,1335,3))

'''
(data are read from the file, and not loaded into memory)
Working on a list of image files
'''


# plt.imshow(img)     
# plt.show()
# plt.savefig('plot.png')

# plt.imsave('red_elephant.png', img[:,:,0], cmap=plt.cm.gray)