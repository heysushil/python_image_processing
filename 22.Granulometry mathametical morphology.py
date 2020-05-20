import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def disk_structure(n):
    # n = [2  6 10 14 18]
    '''
    struct 5 matrixes:
        [5*5],[13*13],[21*21],[29*29],[37*37]
    '''
    struct = np.zeros((2 * n + 1, 2 * n + 1))
    # print(struct)
    # get 5 matrix or same as struct but np.indices provide number in earch x and y from  
    # like as x = [0:] and y = [0:]
    x, y = np.indices((2 * n + 1, 2 * n + 1))
    # print(y)
    # exit()
    mask = (x - n)**2 + (y - n)**2 <= n**2
    struct[mask] = 1
    return struct.astype(np.bool)

# granulometry recived 2 arg
def granulometry(data, sizes=None):
    # s have 256*256 sahpe
    s = max(data.shape)
    # newsize = sizes
    # print(newsize)
    # in case sizes have no value then genereate a sizes value by this if
    if sizes is None:
        sizes = range(1, s/2, 2)
    # \ use for line breack
    '''
    granulo one by one get these numbers
        0:23849 = 2
        1:23287 = 6
        2:14171 = 10
        3:4834 = 14
        4:0 =18
    '''    
    granulo = [ndimage.binary_opening(data, \
            structure=disk_structure(n)).sum() for n in sizes]
    return granulo


np.random.seed(1)
n = 10
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = im > im.mean()

# in range of 2 to 19 get 5 numbers from 0 to 4 = [2  6 10 14 18]
granulo = granulometry(mask, sizes=np.arange(2, 19, 4))
# exit()
plt.figure(figsize=(6, 2.2))

plt.subplot(121)
plt.imshow(mask, cmap=plt.cm.gray)
opened = ndimage.binary_opening(mask, structure=disk_structure(10))
opened_more = ndimage.binary_opening(mask, structure=disk_structure(14))
plt.contour(opened, [0.5], colors='b', linewidths=2)
plt.contour(opened_more, [0.5], colors='r', linewidths=2)
plt.axis('off')

plt.subplot(122)
plt.plot(np.arange(2, 19, 4), granulo, 'ok', ms=8)


plt.subplots_adjust(wspace=0.02, hspace=0.15, top=0.95, bottom=0.15, left=0, right=0.95)
plt.show()