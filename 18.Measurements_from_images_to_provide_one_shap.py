import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

np.random.seed(1)
n = 10
l = 256
im = np.zeros((l, l))
points = l*np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))

mask = im > im.mean()

label_im, nb_labels = ndimage.label(mask)
# above code is same as it is 17th file but the rest is chnaged to remove few more points to provide a shap.

# ndimage.sum method use to sum the mask and label_im matrix togater also the range provide a range in which the sum done.
# like as matix have x and y so the range here is use nb_labels which is holds the union of ndimage.label. That means range have all unique value because nb_labels provide a union of int numbers.
sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))
mask_size = sizes < 1000

# mask_size holds the matrix values which have less value then 1000 and on these points insert a label_im values
remove_pixel = mask_size[label_im]

# on remove_pixel matrix get all the points which want to remove that means to plot 0 on those points. Which is done here.
label_im[remove_pixel] = 0

# at alst using numpy.unique fillter the dublicat values and store all the unqiue matrix values in labels
labels = np.unique(label_im)

'''
np.searchsorted method work as: first value = labels assume as sorted and lable_im is need to be sorted by searching values on lable_im matrix and sort them behalf of the labels matrix. Which is the work of np.searchsorted method.
'''
label_clean = np.searchsorted(labels, label_im)


plt.figure(figsize=(6 ,3))

plt.subplot(121)
plt.imshow(label_im, cmap=plt.cm.nipy_spectral)
plt.axis('off')
plt.subplot(122)
plt.imshow(label_clean, vmax=nb_labels, cmap=plt.cm.nipy_spectral)
plt.axis('off')

plt.subplots_adjust(wspace=0.01, hspace=0.01, top=1, bottom=0, left=0, right=1)
plt.show()