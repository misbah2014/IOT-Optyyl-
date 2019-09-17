import cv2
import numpy as np
from time import sleep

cap1 = cv2.VideoCapture(0)

while True:
    _,frame1 = cap1.read()
    #_,frame2 = cap2.read()
    cv2.imshow("Camera 1", frame1)
   # cv2.imshow("Camera 2", frame2)



