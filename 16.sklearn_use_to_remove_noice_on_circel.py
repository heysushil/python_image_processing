from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering
import numpy as np
import matplotlib.pyplot as plt

l = 100
# x and y are storing matirx postions which use to made full matrix of x and y
x, y = np.indices((l, l))
print('\n\nValue of x = ',x)
print('\n\nValue of y = ',y)

# center use to fix a points in which create a circle by defining redius and then calculate the circle area of each 4's
center1 = (28, 24)
center2 = (40, 50)
center3 = (67, 58)
center4 = (24, 70)
radius1, radius2, radius3, radius4 = 16, 14, 15, 14

# these calculation are use to find bool value in which the false and trues get in each variable
# circle variable have matrix in which the false = 0 and true = 1
# process of creating the circle is = take example of circle4 which the last and yellow colored
'''
Example of circle4:
    center4 define the [24,70], point in which the point created
    radius4 define the round cericle at point [24,70]
    circle4 use formula to product 1 in all possible possitions in x,y matrix by adding 1 at those points.
    that's why when you print cirlce4 in which you start geting true from 13th row to 26th row 
    it's simple concept of log chart of math in which you plot point then circle to the point at same size.
'''
circle1 = (x - center1[0])**2 + (y - center1[1])**2 < radius1**2
circle2 = (x - center2[0])**2 + (y - center2[1])**2 < radius2**2
circle3 = (x - center3[0])**2 + (y - center3[1])**2 < radius3**2
circle4 = (x - center4[0])**2 + (y - center4[1])**2 < radius4**2
# print('\n\ncircle1 = ',circle1)

# after created full circle matrix then stro all of them at one matrix.
# it's simple plot all the cricle points in one graph rather then drwaing them individually
# for best practice you should useing matplot shwo the img variable output to understand the concept
img = circle1 + circle2 + circle3 + circle4

# mask show you the full 4 cirlce in output if you show them using pyplot
mask = img.astype(bool)

# for create corect circular shap need a flot points that's why convert the bool into float
img = img.astype(float)

# it's for creating noise outside of circle
img += 1 + 0.2*np.random.randn(*img.shape)

# Convert the image into a graph with the value of the gradient on
# the edges.
graph = image.img_to_graph(img, mask=mask)
# Take a decreasing function of the gradient: we take it weakly
# dependant from the gradient the segmentation is close to a voronoi
graph.data = np.exp(-graph.data/graph.data.std())

# in this case the matrix have to much value which not understandablt for pyplot to show the result. for that need to normalize the output and the best way is to use the spectral_clustering method 
labels = spectral_clustering(graph, n_clusters=4, eigen_solver='arpack')
label_im = -np.ones(mask.shape)
label_im[mask] = labels

plt.figure(figsize=(12, 5))

# output lenght made small to show the nearest output
# l = 128

plt.subplot(141)
plt.imshow(img[:l, :l])
plt.title('Img', fontsize=20)
plt.axis('off')
plt.subplot(142)
plt.imshow(mask[:l, :l])
plt.title('Mask', fontsize=20)
plt.axis('off')
plt.subplot(143)
plt.imshow(label_im[:l, :l])
plt.axis('off')
plt.title('Label Img', fontsize=20)
# plt.subplot(144)
# plt.imshow(reconstruct_final[:l, :l], cmap=plt.cm.gray)
# plt.imshow(label_im[mask], cmap=plt.cm.gray)
# # plt.contour(label_im[:l, :l], [0.5], linewidths=2, colors='r')
# plt.title('recons final', fontsize=20)
# plt.axis('off')

plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0, right=1)

plt.show()