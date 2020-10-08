import numpy as np
import cv2
from matplotlib import pyplot as plt


cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    #frameBlur = cv2.GaussianBlur(frame,(5,5),0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,threshFrame = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)

    #edges = cv2.Canny(gray,100,200)

    # detect if a phone shows up in frame.. but how?
    # possibly find enclosed region with a certain area?
    #sedgeFrame = edges[100:480, 400:]
    #finalFrame = frameBlur[100:480, 400:]

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()