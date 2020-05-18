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
open_img = ndimage.binary_opening(binary_img)
close_img = ndimage.binary_closing(open_img)

eroded_img = ndimage.binary_erosion(binary_img)
reconstruct_img = ndimage.binary_propagation(eroded_img, mask=binary_img)
tmp = np.logical_not(reconstruct_img)
eroded_tmp = ndimage.binary_erosion(tmp)
reconstruct_final = np.logical_not(ndimage.binary_propagation(eroded_tmp, mask=tmp))

# close_final = np.abs(mask - close_img).mean() 
# print('close final result\n\n',close_final)
# reconsturct_mean_final = np.abs(mask - reconstruct_final).mean()
# print('\n\nreconstruct mean final \n\n\n',reconsturct_mean_final)


plt.figure(figsize=(12, 5))

# output lenght made small to show the nearest output
l = 128

plt.subplot(141)
plt.imshow(binary_img[:l, :l], cmap=plt.cm.gray)
plt.title('Binary Img', fontsize=20)
plt.axis('off')
plt.subplot(142)
plt.imshow(eroded_img[:l, :l], cmap=plt.cm.gray)
plt.title('eroded img', fontsize=20)
plt.axis('off')
plt.subplot(143)
plt.imshow(reconstruct_img[:l, :l], cmap=plt.cm.gray)
plt.axis('off')
plt.title('reconstruct', fontsize=20)
plt.subplot(144)
# plt.imshow(reconstruct_final[:l, :l], cmap=plt.cm.gray)
plt.imshow(mask[:l, :l], cmap=plt.cm.gray)
plt.contour(reconstruct_final[:l, :l], [0.5], linewidths=2, colors='r')
plt.title('recons final', fontsize=20)
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)

plt.show()