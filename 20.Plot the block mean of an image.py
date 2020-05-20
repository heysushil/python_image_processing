'''
# Introduction about scipy and ndimage method which use here

1. scipy.misc.face(gray=True) = use to feath degault image
2. f.shpae get the dimention of image in this case is (768*1024) width * height
3. X and Y using np.ogrid create a matrix or 0:768 and 0*1024
4. regions produce a 300 list of 3D array from 000:299.
    Explain about regions positions:
        1. 000 => position again holds matrix of [000:299] 
        2. and on this matrix have 0 to 49 number on each position
        3. the sequens of numbering is after each 6 possition number increse by 1
        4. Example  [000:005] = 0
                    [006:011] = 1 and so on.....
5. block_mean also have 3D array in which the 
    1. first array range [000:192]
    2. inner array range [000:172] : these all are list of 1D array and have flot values range on it. Like as this 1D array have range and datatype as follows:
        dtype:dtype('float64')
        max:171.20833333333334
        min:26.916666666666668
    3. These values came up by the calculation on block_mean
6. block_mean.shap got the new shap which is:
    0:192
    1:170
    len():2
'''

import numpy as np
import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

f = scipy.misc.face(gray=True)
sx, sy = f.shape
X, Y = np.ogrid[0:sx, 0:sy]

regions = sy//6 * (X//4) + Y//6
block_mean = ndimage.mean(f, labels=regions, index=np.arange(1, regions.max() +1))
block_mean.shape = (sx//4, sy//6)

plt.figure(figsize=(5, 5))
plt.imshow(block_mean, cmap=plt.cm.gray)
plt.axis('off')

plt.show()