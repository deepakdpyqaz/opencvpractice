import numpy as numpy
import cv2

cap1=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('resources/vlog.avi',fourcc,20.0,(640,480))

while (cap2.isOpened() and cap1.isOpened()):
    ret1,frame1=cap1.read()
    ret2,frame2=cap2.read()
    if(ret1 and ret2):
        frame1=cv2.resize(frame1,(200,200))
        frame2=cv2.resize(frame2,(640,480))
        frame2[280:,440:]=frame1
        cv2.imshow('video',frame2)
        out.write(frame2)
        if(cv2.waitKey(1)==ord('q')):
            cv2.destroyAllWindows()
            break
    else:
        cv2.destroyAllWindows()
        break
cap1.release()
cap2.release()
out.release()