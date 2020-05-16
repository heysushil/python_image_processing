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

mask = (im > im.mean()).astype(np.float)
# upar ka process same to same hai historgram segmentation jaisa

img = mask + 0.3*np.random.randn(*mask.shape)

binary_img = img > 0.5
print('binary imag ',binary_img)
# Remove small white regions binaroy opening remove the 1 from corner
open_img = ndimage.binary_opening(binary_img)
print('open img ',open_img)
# Remove small black hole.
close_img = ndimage.binary_closing(open_img)
print('close img ',close_img)

plt.figure(figsize=(12, 3))

# output lenght made small to show the nearest output
l = 128

plt.subplot(141)
plt.imshow(binary_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(142)
plt.imshow(open_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(143)
plt.imshow(close_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(144)
plt.imshow(mask[:l, :l], cmap=plt.cm.gray)
plt.contour(close_img[:l, :l], [0.5], linewidths=2, colors='r')
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)

plt.show()