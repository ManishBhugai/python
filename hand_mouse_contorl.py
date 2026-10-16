from timeit import main

import cv2
import pyautogui
import numpy as np
import mediapipe as mp
import time

cam=cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot open camera")
    exit()
    
else:
    while True:
        ret,frame=cam.read()
        frame=cv2.flip(frame,1)
        
        if not ret:
            print("cant retrive the frame")
            break 
        else:
            cv2.imshow("frame",frame)
            cv2.waitKey(1)
            
cam.release()
cv2.destroyAllWindows()


            
            
        