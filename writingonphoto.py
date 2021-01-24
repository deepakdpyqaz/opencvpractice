import numpy as np 
import cv2
import time

height=400
width=800
xspeed=5
yspeed=5
img=np.zeros((height,width,3),dtype=np.uint8)
cv2.line(img,(width//2,0),(width//2,height),(255,255,255),2)
x,y=(10,10)
cv2.circle(img,(x,y),5,(255,255,255),cv2.FILLED)
while True:
    cv2.circle(img,(x,y),5,(0,0,0),cv2.FILLED)
    time.sleep(0.05)
    x+=xspeed
    y+=yspeed
    if(x>800):
        x=10
        yspeed=5
    if(y>400):
        yspeed=-5
    cv2.circle(img,(x,y),5,(255,255,255),cv2.FILLED)
    cv2.imshow('image',img)
    if(cv2.waitKey(1)==ord('q')):
        cv2.destroyAllWindows()
        break
