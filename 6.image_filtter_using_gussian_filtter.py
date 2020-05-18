import scipy.misc
from scipy import ndimage
import matplotlib.pyplot as plt

face = scipy.misc.face(gray=True)

# gaussina filter use sigma to blur the image
blurred_face = ndimage.gaussian_filter(face, sigma=0)
very_blurred = ndimage.gaussian_filter(face, sigma=20)
# uniform use binay data form with size to blure the image
local_mean = ndimage.uniform_filter(face, size=0)

# figure values are x = 12 (width of output box) and y = 3 (height of output box)
plt.figure(figsize=(12, 3))
# subplot value the define the image size
plt.subplot(131)
# imshow use show the output. 1st paremeter is the value of image and cmap is use to made it gray
plt.imshow(blurred_face, cmap=plt.cm.gray)
# axis off use to off metplot's defalut axis on properti
plt.axis('off')
plt.subplot(132)
plt.imshow(very_blurred, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(local_mean, cmap=plt.cm.gray)
plt.axis('off')
# sublots_adjust use to adjest the new plot areat of image
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                    left=0.01, right=0.99)

plt.show()