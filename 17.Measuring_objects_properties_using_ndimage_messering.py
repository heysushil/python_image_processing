# 2.6.6. Measuring objects properties: ndimage.measurements

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

np.random.seed(1)
n = 10
l = 256

im = np.zeros((l, l))

# after creating im variable which holds 256*256 matrix of zeors is use to plot points in all matrix fields.
points = l*np.random.random((2, n**2))

# made 1 at this point range
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1

# sigma is not only use to blure the image but also modify the outer circle of shape. like as in sigma provide a formula whcih use to show a multiple shapes in image but if you change this wiht random numbers you will get different shapes.
# like change sigma value with sigma=5.2282277 then check or change with other value then chack again.
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = im > im.mean()

# this is use to set all 0 as background and rest of 1's are using to show the mask designing
label_im, nb_labels = ndimage.label(mask)

plt.figure(figsize=(9,3))

plt.subplot(131)
plt.imshow(im)
plt.axis('off')
plt.subplot(132)
plt.imshow(mask, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(label_im, cmap=plt.cm.nipy_spectral)
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=1)
plt.show()