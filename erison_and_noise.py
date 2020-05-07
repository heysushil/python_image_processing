import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# ZERO WALA MATRIX BANAYA
a = np.zeros((5,5), dtype=np.int)
print('\n',a)

# matix me matrix postion 11 se 13, aur same 21, 31 tak banaya
a[1:4, 1:4] = 1; 
# ek extra 1 add kiya gaya hai 44 postion pe
a[4, 4] = 1
print('\n',a)

# Opening removes small objects
# yaha small object wo 44 wali postion ka 1 hai jisko remove kiya gaya hai
smallremove = ndimage.binary_opening(a, structure=np.ones((3,3))).astype(np.int)
print('\n',smallremove)

# Opening can also smooth corners
# smooth corners means sare corner edges ko remove kar diya hai
smoothremove = ndimage.binary_opening(a).astype(np.int)
print('\n',smoothremove)

# -----------FINAL 3 RIGHT BOXEX GENERATE BY THIS AREA-------------------------------
square = np.zeros((32, 32))
square[10:-10, 10:-10] = 1
np.random.seed(2)
# random number me 2 = 2 digit random number generate,  20 = 20 random number length
x, y = (32*np.random.random((2, 20))).astype(np.int)
print(x)
print(y)
square[x, y] = 1
# 3 alag ndimage method ka use karke 3 alag input generate kiya gaya hai 
open_square = ndimage.binary_opening(square)
eroded_square = ndimage.binary_erosion(square)
reconstruction = ndimage.binary_propagation(eroded_square, mask=square)
# -----------END RIGHT 3 BOX AREA----------------------------------------------------

# plt figure ka use output box ki size ke liye kiya gaya hai
plt.figure(figsize=(12, 5))
# subplot ka use agar 1 se jada image show karana hai to uski size aur space ke liye use hota hai.
# subplot ki value 3 digit me 111 se max honi cahiye
# agar ek sath 2 image dikhana hai to 121, 122 or 4 hai to 141,142...144
plt.subplot(151)
# iska use input ko get kar ke iske base be output generate karna hota hai
plt.imshow(smallremove, cmap=plt.cm.gray, interpolation='nearest')
# jab ek se jata image ko single output box me show karana ho ya custom axis input ho to use karte hai
plt.axis('off')
plt.title('Small Remove', fontsize=20)
plt.subplot(152)
plt.imshow(smoothremove, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.title('Smooth Remove', fontsize=20)

# ------------3 RIHGT OUTPUT BOX SHOW KARANE KE LIYE--------------------------------
plt.subplot(153)
plt.imshow(square, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.title('Squares', fontsize=20)
plt.subplot(154)
plt.imshow(open_square, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.title('Open Square', fontsize=20)
plt.subplot(155)
plt.imshow(reconstruction, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')
plt.title('Reconstruction', fontsize=20)
# ------------END 3 RIHGT OUTPUT BOX SHOW KARANE KE LIYE--------------------------------
# jab 1 se jada image show karna hota hai to unke bich me space ke liye use karte hai
plt.subplots_adjust(wspace=0, hspace=0.02, top=0.99, bottom=0.01, left=0.01, right=0.99)
# isse output ko show kiya gaya hai
plt.show()

