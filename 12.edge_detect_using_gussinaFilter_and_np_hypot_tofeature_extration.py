import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
print('\nnormal im',im)
'''
Rotate an array.

The array is rotated in the plane defined by the two axes given by the axes parameter using spline interpolation of the requested order.
'''
im = ndimage.rotate(im, 15, mode='constant')
print('\nrotated im',im)
# image me 0 add karna image ko smooth karne ke liye, aur 8 ye sigma value hai
# sigma value jo filete output hai usko blur karne ke liye hai .
# example 0=no blur, 8=more blure
im = ndimage.gaussian_filter(im, 8)
print('\ngaussina filter im',im)

# sobel method filttering ke liye use hua hai isme axis x, x axis ko highlight kar raha hai
sx = ndimage.sobel(im, axis=0, mode='constant')
print('\nsobel axis 0',im)
# ye y axis ko highlight kar raha hai
sy = ndimage.sobel(im, axis=1, mode='constant')
print('\nsobel axis 1',im)
# axis -1 default case hai isme axis y rahta hai
sxy = ndimage.sobel(im, axis=-1, mode='constant')
sob = np.hypot(sx, sy)
print('\n hypot',im)

plt.figure(figsize=(12, 3))
plt.subplot(161)
plt.imshow(im, cmap=plt.cm.gray)
plt.axis('off')
plt.title('square', fontsize=20)
plt.subplot(162)
plt.imshow(sx)
plt.axis('off')
plt.title('Sobel X', fontsize=20)
plt.subplot(163)
plt.imshow(sy)
plt.axis('off')
plt.title('Sobel Y', fontsize=20)
plt.subplot(164)
plt.imshow(sxy)
plt.axis('off')
plt.title('Sobel XY', fontsize=20)
plt.subplot(165)
plt.imshow(sob)
plt.axis('off')
plt.title('Hypot', fontsize=20)

# im value with rotated matirx
# im = im + 0.07*np.random.random(im.shape)
im += 0.07*np.random.random(im.shape)

sx = ndimage.sobel(im, axis=0, mode='constant')
sy = ndimage.sobel(im, axis=1, mode='constant')
sob = np.hypot(sx, sy)

plt.subplot(166)
plt.imshow(sob)
plt.axis('off')
plt.title('Sobel Noice', fontsize=20)



plt.subplots_adjust(wspace=0.02, hspace=0.02, top=1, bottom=0, left=0, right=0.9)

plt.show()