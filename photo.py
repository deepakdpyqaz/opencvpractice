import cv2
import numpy as np

# Reading an image 
img=cv2.imread('resources/lena.jpg')

# Getting the current size of image
a=img.shape
print(a)
width=a[0]
height=a[1]

# Resizing the image 
imgResized=cv2.resize(img,(width//2,height//2))

#cropping an image
imgCropped=img[0:200,0:200]

# converting color scheme of an image 
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blur an image 
imgBlur=cv2.GaussianBlur(img,(17,17),0)

# Edge Detection
imgCanny = cv2.Canny(img,22,20)
# Displaying an image
# cv2.imshow('image',img)
# cv2.imshow('imageResized',imgResized)
# cv2.imshow('imageCropped',imgCropped)
# cv2.imshow('imageGray',imgGray)
# cv2.imshow('imageBlur',imgBlur)
cv2.imshow('imageCanny',imgCanny)

while True:
    if cv2.waitKey(1)==ord('q'):
        cv2.destroyAllWindows()
        break