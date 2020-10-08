import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#orange = np.uint8([[[255,69,0 ]]])
#hsv_orange = cv2.cvtColor(orange,cv2.COLOR_BGR2HSV)
#print(hsv_orange)

while(1):

    # Take each frame
    ret, frame = cap.read()

    # gaussian filter
    frameBlur = cv2.GaussianBlur(frame,(5,5),0)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frameBlur, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lower_hsv = np.array([145,100,150])
    upper_hsv = np.array([175,255,255])

    # Threshold the HSV image to get only desired colors
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    contours,hierarchy = cv2.findContours(mask, 1, 2)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cnt = contours[0]
    M = cv2.moments(cnt)

    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.rectangle(frame, (cx-5, cy-5), (cx+5, cy+5), (0, 255, 0))

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()