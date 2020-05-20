# 2.6.8.12. Find the bounding box of an object

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

# Find the largest connected component
sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))
mask_size = sizes < 1000
remove_pixel = mask_size[label_im]
label_im[remove_pixel] = 0
labels = np.unique(label_im)
label_im = np.searchsorted(labels, label_im)
# print('Lable im final values: ',label_im)
# Now that we have only one connected component, extract it's bounding box
'''
# find_objects have syntax: scipy.ndimage.find_objects(input, max_label=0)[source]
1. in which the input have lable more then 0 other wise ignore it
2. Maximum label to be searched for in input. If max_label is not given, the positions of all objects are returned.
3. [0] is provide the range in which the object finds. also when you change 0 to other value it shwos you range error becauase label_im matrix filttered and have all unique value on it.
4. find_obects 1st argument label_im==4 slice the matrix into 2 slices with the range.
5. when you zoom the output you will se the bounding boxes which produced by the find_objects method
'''
# newobj = ndimage.find_objects(label_im==4)[0]
# print(newobj)
# exit()

'''
# For better understanding to find_objects also follow these urls
1. https://stackoverflow.com/questions/36200763/objects-sizes-along-dimension
2. https://www.programcreek.com/python/example/93927/scipy.ndimage.find_objects
3. https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.find_objects.html
'''
slice_x, slice_y = ndimage.find_objects(label_im==5)[0]

# at last roi made a 3D array which show you output in whcih if you zoom. you show the ranged pixcels.
roi = im[slice_x, slice_y]

plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.imshow(label_im, cmap=plt.cm.nipy_spectral)
plt.axis('off')
# custom axes arrguments = plt.axes((left, bottom, width, height), facecolor='w')
plt.subplot(132)
# plt.axes([0, 0, 1, 1])
plt.imshow(roi)
plt.axis('off')

plt.show()