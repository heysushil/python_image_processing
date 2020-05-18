# USE MISC TO GET TO SHOW THE IMAGE BY MATPLOTLIB.PYPLOT LIBRARY
from scipy import misc
# Insted of scipy.misc.imsave use imageio libaray becaue in scipy version 1.2 imsave was removed
import imageio
# Get a 1024 x 768, color image of a raccoon face.
f = misc.face()
imageio.imwrite('face.png', f) # Write an image to the specified file.
# pyplot use to show the output
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()