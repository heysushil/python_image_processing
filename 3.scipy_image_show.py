# misc is changed to imageio.imwrite in version >= 1.2 
from scipy import misc
import imageio
face = misc.face()

imageio.imwrite('face.png', face) # uses the Image module (PIL)

face = imageio.imread('face.png')
# print(type(face))
# type(face)

face.shape, face.dtype

# import matplotlib.pyplot as plt
# plt.imshow(f)
# plt.show()

import numpy as np
# STORE NUMPY ARRAY DATA INTO RAW DATA BY CREATIN NEW RAW FILE = FACE.RAW
face.tofile('face.raw') # Create raw file
face_from_raw = np.fromfile('face.raw', dtype=np.uint8) # 8-bit datatype
face_from_raw.shape

face_from_raw.shape = (768, 1024, 3)

# shape is holds x, y and image dimention 3D
face_memmap = np.memmap('face.raw', dtype=np.uint8, shape=(768, 1024, 3))

for i in range(10):
    im = np.random.randint(0, 256, 10000).reshape((100, 100))
    misc.imsave('random_%02d.png' % i, im)

# glob use to create random image list
from glob import glob
filelist = glob('random*.png')
filelist.sort()
# print(data)

f = misc.face(gray=True)  # retrieve a grayscale image


face[0, 40]

# Slicing
face[10:13, 20:23]



face[100:120] = 255

lx, ly = face.shape
X, Y = np.ogrid[0:lx, 0:ly]
mask = (X - lx / 2) ** 2 + (Y - ly / 2) ** 2 > lx * ly / 4
# Masks
face[mask] = 0
# Fancy indexing
face[range(400), range(400)] = 255

import matplotlib.pyplot as plt
# plt.imshow(f, cmap=plt.cm.gray)
# plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200)        

# Remove axes and ticks
# plt.axis('off')
# plt.contour(f, [50, 200])

# plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='bilinear')        
# plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='nearest') 

plt.show()