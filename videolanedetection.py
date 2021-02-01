import numpy as np 
import cv2


def makecoordinates(image, params):
    slope, intercept = params
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    return np.array([x1, y1, x2, y2])


def region_of_interest(img_cany):
    trianle = np.array([[(560, 280), (285, 700), (1070, 700)]], dtype=np.int32)
    mask = np.zeros_like(img_cany)
    cv2.fillPoly(mask, trianle, 255)
    img2 = cv2.bitwise_and(img_cany, mask)
    return img2


def draw_lines(image, lines):
    line_image = np.zeros_like(image)
    left_side = []
    right_side = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            slope, intercept = np.polyfit((x1, x2), (y1, y2), 1)
            if slope < 0:
                left_side.append((slope, intercept))
            else:
                right_side.append((slope, intercept))
    left_side_avg = np.average(left_side, axis=0)
    right_side_avg = np.average(right_side, axis=0)
    left_line = makecoordinates(image, left_side_avg)
    right_line = makecoordinates(image, right_side_avg)
    cv2.line(image, (left_line[0], left_line[1]),
             (left_line[2], left_line[3]), (255, 0, 0), 5)
    cv2.line(image, (right_line[0], right_line[1]),
             (right_line[2], right_line[3]), (255, 0, 0), 5)
    return image


cap=cv2.VideoCapture('resources/lane.mp4')

while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret):
        img=np.copy(frame)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
        img_cany = cv2.Canny(img_blur, 50, 150, 0)
        region = region_of_interest(img_cany)

        lines = cv2.HoughLinesP(region, 2, np.pi/180, 100,minLineLength=40, maxLineGap=5)
        lanes = draw_lines(frame, lines)
        cv2.imshow('lanes',lanes)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
