import numpy as np
from PIL import Image
# import matplotlib.image as image
import matplotlib.pyplot as plt
from scipy import ndimage
import seaborn as sb
from sklearn import io, color

lina_color = io.imread(path+img)
lina_gray = color.rgb2gray(lina_color)
img = Image.open('microarray/data/gdsDraw.png')

plt.imshow(img)
plt.show()
exit()

# fetch the image
img = Image.open('microarray/data/gdsDraw.png')

# img.shape provide dimention and color fomate like in this case it's 3 = RGB
# img.shape, img.dtype
# conver image to numpy array
img2array = np.asarray(img)
imgshap = img2array.shape
imgdatatype = img2array.dtype
# print(img2array)
# create pillow image
# pillowimageByNPArray = Image.fromarray(img2array)
# pillowimageSave = Image.fromarray(img2array).save('microarray/data/arrayImag.png')

# slicing image
smallone = img2array[00:84, 255:300] > 254

plt.figure(num=2,figsize=(8,6))
# plt.annotate(s, smallone)
plt.imshow(smallone)
plt.show()
exit()
# for showing image
plt.figure(figsize=(12, 3))
plt.subplot(401)
plt.imshow(newimg, cmap=plt.cm.gray)
plt.axis('off')
# plt.subplot(402)
# plt.imshow(blurImg, cmap=plt.cm.gray)
# plt.axis('off')
# plt.subplot(403)
# plt.imshow(veryBlurImg, cmap=plt.cm.gray)
# plt.axis('off')
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01, 
                    left=0.01, right=0.99)
plt.show()
