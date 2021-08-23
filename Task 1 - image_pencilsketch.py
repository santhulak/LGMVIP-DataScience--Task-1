import cv2
import numpy as np
#Reads the image
img = cv2.imread("3.jpg")
#resize the window
img = cv2. resize(img, (300, 300))
#converts the image to grayscale
greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#convert rge gray scale to inverted gray scale
invert_gray_image = 255-greyimg
#blur / smooth the image -
smooth = cv2.GaussianBlur(invert_gray_image,(21,21),sigmaX=0)
#invert the smoothened image
invert_smooth = 255-smooth
#to display in sketch mode
pencilsketch=cv2.divide(greyimg,invert_smooth,scale=256.0)
#display the original image
pencilsketch = cv2. resize(pencilsketch, (300, 300))

cv2.imshow("Original Image", img)

cv2.imshow("GreyScale",greyimg)
cv2.imshow("Inverted gray image",invert_gray_image)
cv2.imshow("Smoothened image",smooth)
cv2.imshow("Invert smoothened image",invert_smooth)
cv2.imshow("Pencil Sketch",pencilsketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
