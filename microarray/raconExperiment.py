import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import misc

# fetch racon face
racconImg = misc.face()

# conver image into nparray
arrayOfRacconImg = np.asarray(racconImg)

# sliciing shape:(768, 1024, 3)
imgslicing = arrayOfRacconImg[000:600, 200:1024]
# pillow to fectch image
fetchImageByPillow = Image.fromarray(arrayOfRacconImg)

# output
plt.imshow(imgslicing)
plt.show()

