# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4081273/

'''
Abstract
scikit-image is an image processing library that implements algorithms and utilities for use in research, education and industry applications. It is released under the liberal Modified BSD open source license, provides a well-documented API in the Python programming language, and is developed by an active, international team of collaborators. In this paper we highlight the advantages of open source to achieve the goals of the scikit-image library, and we showcase several real-world image processing applications that use scikit-image. More information can be found on the project homepage, http://scikit-image.org.

Introduction
In our data-rich world, images represent a significant subset of all measurements made. Examples include DNA microarrays, microscopy slides, astronomical observations, satellite maps, robotic vision capture, synthetic aperture radar images, and higher-dimensional images such as 3-D magnetic resonance or computed tomography imaging. Exploring these rich data sources requires sophisticated software tools that should be easy to use, free of charge and restrictions, and able to address all the challenges posed by such a diverse field of analysis.

This paper describes scikit-image, a collection of image processing algorithms implemented in the Python programming language by an active community of volunteers and available under the liberal BSD Open Source license. The rising popularity of Python as a scientific programming language, together with the increasing availability of a large eco-system of complementary tools, makes it an ideal environment in which to produce an image processing toolkit.

-----------------------------------------------------------------------------------------------

The project aims are:

1. To provide high quality, well-documented and easy-to-use implementations of common image processing algorithms.

Such algorithms are essential building blocks in many areas of scientific research, algorithmic comparisons and data exploration. In the context of reproducible science, it is important to be able to inspect any source code used for algorithmic flaws or mistakes. Additionally, scientific research often requires custom modification of standard algorithms, further emphasizing the importance of open source.

2. To facilitate education in image processing.

The library allows students in image processing to learn algorithms in a hands-on fashion by adjusting parameters and modifying code. In addition, a novice module is provided, not only for teaching programming in the “turtle graphics” paradigm, but also to familiarize users with image concepts such as color and dimensionality. Furthermore, the project takes part in the yearly Google Summer of Code program1, where students learn about image processing and software engineering through contributing to the project.

3. To address industry challenges.

High quality reference implementations of trusted algorithms provide industry with a reliable way of attacking problems without having to expend significant energy in re-implementing algorithms already available in commercial packages. Companies may use the library entirely free of charge, and have the option of contributing changes back, should they so wish.

'''

'''
Getting started
One of the main goals of scikit-image is to make it easy for any user to get started quickly—especially users already familiar with Python’s scientific tools. To that end, the basic image is just a standard NumPy array, which exposes pixel data directly to the user. A new user can simply load an image from disk (or use one of scikit-image’s sample images), process that image with one or more image filters, and quickly display the results:
'''

from skimage import data, io
# import skimage.filters as filter

import numpy as np
import matplotlib.pyplot as plt

# Load a small section of the image.
image = data.coins()[0:95, 70:370]

fig, axes = plt.subplots(ncols=2, nrows=3,
                         figsize=(8, 4))
ax0, ax1, ax2, ax3, ax4, ax5  = axes.flat
ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Original', fontsize=24)
ax0.axis('off')
