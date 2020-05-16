import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

np.random.seed(1)
# do variable liye gaye hai n = number and l = length
n = 10
l = 256
# 256*256 ka zero ka matrix creat kiya gaya
im = np.zeros((l, l))
# single astix means 10 multiply 2 but double ** means 10 * 10
# print('\nn**2 ka output\n\n',n**2)
# random(2,10) matrix of 2*10
points = l*np.random.random((2, n**2))
# print('\nPoints jinka use matrix me 1 plot karne ke liye kiya jayega\n\n',points)
# im[] range me 1 set kiya gaya hai taki matrix ke alag alag points pe boxes creat kiya jaye
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
# filter me sigma use kiya gaya hai blur karne ke liy
# gussain_filter provide matrix which use to plot point and blur the output using the sigma number
im = ndimage.gaussian_filter(im, sigma=l/(4.*n))
# mask variable ka use kiya gaya hai plot points banae ke liye.
mask = (im > im.mean()).astype(np.float)

mask += 0.1 * im
# *mask.shape 256*256 ka sahpe provide kar raha hai jiske liye random number ka matrix bana rahe hai
# print('mask shape ',mask.shape)
img = mask + 0.2*np.random.randn(*mask.shape)
print('\n\nfinal img\n\n',img)
# ye histogram banae ke liye use ho raha hai
# hist = historgram, bin_edges = binary edges
# bins= 60 , 60 flot point number generate karega, jo ki bin_edges me recive hoga
hist, bin_edges = np.histogram(img, bins=60)
# hist histogram points recive karega jo historgram graph banayega
# print(hist)
# print(bin_edges)
# center red line create karne ke liye points
bin_centers = 0.5*(bin_edges[:-1] + bin_edges[1:])

# binary_img varaible use kiya gaya hai ki jo img value hai unmese output me mask hai usme se noise remove karne ke liye
binary_img = img > 0.5
print('\n\nbinary imag value ',binary_img)
plt.figure(figsize=(11,4))

plt.subplot(131)
plt.imshow(img)
plt.axis('off')
plt.subplot(132)
# lw = line weight
plt.plot(bin_centers, hist, lw=2)
# ls = line style 
plt.axvline(0.5, color='r', ls='solid', lw=2)
plt.text(0.57, 0.8, 'histogram', fontsize=20, transform = plt.gca().transAxes)
# hide the y axis label values
plt.yticks([])
plt.subplot(133)
# ye 2 commented line ka use karke jitna white hisa hai usko red border se highlight kar sakte hai
# plt.imshow(mask[:l, :l], cmap=plt.cm.gray)
# plt.contour(binary_img[:l, :l], [0.5], linewidths=2, colors='r')
plt.imshow(binary_img, cmap=plt.cm.gray, interpolation='nearest')
plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)
plt.show()