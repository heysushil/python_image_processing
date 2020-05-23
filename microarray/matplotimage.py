import numpy as np
from PIL import Image
# import matplotlib.image as image
import matplotlib.pyplot as plt
from scipy import ndimage

# fetch the image
img = Image.open('microarray/data/gdsDraw.png')
# img.shape provide dimention and color fomate like in this case it's 3 = RGB
# img.shape, img.dtype
# conver image to numpy array
img2array = np.asarray(img)
print(img2array.shape,img2array.dtype)

# create pillow image
pillowimageByNPArray = Image.fromarray(img2array)
pillowimageSave = Image.fromarray(img2array).save('microarray/data/arrayImag.png')

# slicing image
croppedImg = img2array[00:84, 254:1335]
newimg = Image.fromarray(croppedImg)

# blur image by gussain filter
# blurImg = ndimage.gaussian_filter(newimg, sigma=3)
# veryBlurImg = ndimage.gaussian_filter(croppedImg, sigma=9)

# median by ndimage median fillter
medianofImg = ndimage.median_filter(newimg, )

# for one result
plt.imshow(medianofImg)
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
