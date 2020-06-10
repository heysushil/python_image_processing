# you need to download these 2 librarys to find the differen b/w 2 images


'''
Packages for standard desktop environments (Windows, macOS, almost any GNU/Linux distribution)

run pip install opencv-python if you need only main modules

Best to install "opencv-contrib-python" this library for opencv
run pip install opencv-contrib-python if you need both main and contrib modules (check extra modules listing from OpenCV documentation)
'''


import cv2
import numpy as np


# cv2.imreade use to load the image
# I'm used 2 images to find the diff b/w them
# on img folder in repository have 3 images face.png and face2.png are same images and if you run the code with those images you get if condition
image1 = cv2.imread("img/student.png")
# face2 and face.png are same imgaes
# face1 is different image. in this image have one black line at left down corner
image2 = cv2.imread("img/student2.png")


'''
cv2's method subtract fetch the both images or in simple way says that the subtract method subtracting array of image if found any different b/w both images
'''
difference = cv2.subtract(image1, image2)

'''
Then the difference answer will put in numpys any method which find if difference matix values are zero then result in if condition will be true and show the message other wise show the else and also the difference arean on image will be save as result on img folder whcih you will check on img folder and found the difference b/w both images.
'''
result = not np.any(difference) #if difference is all zeros it will return False

if result is True:
    print("The images are the same")
else:
    # cv2's imwrite use to create a image from matrix of difference and show the matrix 1 possition area
    cv2.imwrite("img/result.png", difference)
    print("the images are different")
	
'''
remeber that on previous class we worded on images and there matrix 0 (zero) and 1 same case happend here. difference method of cv2 will generate the matrix of one on that area which is differ then first image and show the ploted area of that matrix other wise on other case it will generate matrix of zero and have no difference.
'''