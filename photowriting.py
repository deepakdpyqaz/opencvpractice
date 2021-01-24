import numpy as np 
import cv2

img=np.zeros((500,500,3),dtype=np.uint8)
img[:,:,:]=255

# drawing a line 
cv2.line(img,(0,0),(500,500),(255,255,0),2)
cv2.line(img,(0,500),(500,0),(0,255,255),2)

# drawing a circle
cv2.circle(img,(250,250),50,(0,0,0),-1)

# drawing a rectangle
cv2.rectangle(img,(10,10),(200,200),(230,126,100),-1)

# writing text 
cv2.putText(img,"Some unique shapes",(100,50),cv2.FONT_HERSHEY_TRIPLEX,1,(67,27,0))
cv2.imshow('image',img)
cv2.waitKey(0)