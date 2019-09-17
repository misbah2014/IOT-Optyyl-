import cv2
import numpy as np
from time import sleep
import RPi.GPIO as GPIO


relay = 21
signal = 12
found  = 0
done = 0

def nothing(x):
    pass

cap = cv2.VideoCapture(0);
GPIO.setwarnings(False)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay, GPIO.OUT)
    GPIO.setup(signal, GPIO.IN)
    GPIO.output(relay, GPIO.HIGH)
except RuntimeError:
    print('GPIO Setup error')
    exit(1)
# brown color 98 172 202
# orange color 103 242 250 103 252 255
# red color 116 242 250
lower_orange = np.array([8,84,103])
upper_orange = np.array([20,113,125])
lower_brown = np.array([0,0,76])
upper_brown = np.array([19,59,110])
lower_red = np.array([100,100,100])
upper_red = np.array([170,255,255])
f=0
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    result = 0
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
             if res[i,j][0] >0:

                if result > 3000:
                    break
                else:
                    result += 1
    print(result)
    #cv2.imshow("mask", frame)
    #cv2.imshow("res", res)
	if GPIO.input(signal):
        try:
         if result >=1300 and done == 0:
            done=1
            print('Relay ON')
            GPIO.output(relay, GPIO.LOW)
            sleep(8)
            GPIO.output(relay, GPIO.HIGH)
            print('Relay OFF')
            sleep(2)
            print('FOUND')

         else:
            print('NOT FOUND')


         except RuntimeError:
            print('Unexcepted error...')
            exit(1)
            key = cv2.waitKey(1)
            if key == 27:
             break
    else:
        print('get input waiting...')
        done = 0

cap.release()
cv2.destroyAllWindows()
