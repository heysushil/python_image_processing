import numpy as np #fetch the numpy library
import matplotlib.pyplot as plt #import the matplotlib's pyplot module
import matplotlib

from skimage import data

# Specific images
matplotlib.rcParams['font.size'] = 18
# print(matplotlib.rcParams['font.size'])

# Stereo images - get bike image on side by side by this exampel
# By submodul pyplot of matplotlib given row coloum and size of image
# in function box 1= row, 2 = column, figsize = show ouput box size
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
# print(fig,axes) # fig and axes fetch the axises of the image by which show 2 images side by side
ax = axes.ravel() #now fetch the fig and axes on tuble
# print(ax[0],'\n')
# print(ax)

images = data.stereo_motorcycle() # geting the motorcycle image
ax[0].imshow(images[0]) # for 1st iamge
ax[1].imshow(images[1]) # for second image

fig.tight_layout() # get the layout how to show the image on outpur
plt.show() # by submodul pyplot show the images side by side




