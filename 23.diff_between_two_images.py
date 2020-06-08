'''
For getting diff b/w 2 images use these libraries if don't have install it or update them

Image Difference with OpenCV and Python

pip install --upgrade scikit-image
pip install --upgrade imutils
pip install opencv-contrib-python

'''

# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
ap.add_argument("-s", "--second", required=True,
	help="second")
args = vars(ap.parse_args())
print(args)
# load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)