# misc is changed to imageio.imwrite in version >= 1.2 
from scipy import misc
face = misc.face()

misc.imsave('face.png', face) # uses the Image module (PIL)

face = misc.imread('face.png')
# print(type(face))
type(face)

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
import matplotlib.pyplot as plt
# plt.imshow(f, cmap=plt.cm.gray)
# plt.imshow(f, cmap=plt.cm.gray, vmin=30, vmax=200)        

# Remove axes and ticks
# plt.axis('off')
# plt.contour(f, [50, 200])

# plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='bilinear')        
plt.imshow(f[320:340, 510:530], cmap=plt.cm.gray, interpolation='nearest') 

plt.show()