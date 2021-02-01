import cv2
import numpy as np

#creating a required area field
def getrequiredarea(img,pts):
    img2=np.zeros_like(img)
    cv2.fillPoly(img2,pts,(255))
    newimg=cv2.bitwise_and(img,img,mask=img2)
    return newimg

image=cv2.imread('resources/lane3.jpg')

img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
img=cv2.resize(img,(700,700))
img2=np.copy(img)
img=cv2.GaussianBlur(img,(5,5),0)
img=cv2.Canny(img,50,150)
img=getrequiredarea(img,np.array([[(250,700),(700,430),(360,380)]],dtype=np.int32))
lines = cv2.HoughLinesP(img,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=60)

for line in lines:
    x1,y1,x2,y2=line.reshape(4)
    # a=np.cos(theta)
    # b=np.sin(theta)
    # x0=a*rho
    # y0=b*rho
    # x1=int(x0+1000*(-b))
    # y1=int(y0+1000*a)
    # x2=int(x0-1000*(-b))
    # y2=int(y0-1000*a)
    cv2.line(img2,(x1,y1),(x2,y2),(0,0,255),10)

cv2.imshow('images',img2)

cv2.waitKey(0)







# cv2.waitKey(0)
