import cv2
import numpy as np

def getrequiredarea(img,pts):
    img2=np.zeros_like(img)
    cv2.fillPoly(img2,pts,(255))
    newimg=cv2.bitwise_and(img,img,mask=img2)
    return newimg

image=cv2.imread('resources/lane4.jpg')

img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(700,700))
img2=np.copy(img)
img=cv2.GaussianBlur(img,(5,5),0)
img=cv2.Canny(img,50,150)
img=getrequiredarea(img,np.array([[(250,700),(700,430),(360,380)]],dtype=np.int32))
lines = cv2.HoughLinesP(img,1,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2=line.reshape(4)
    cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('images',img2)

cv2.waitKey(0)







