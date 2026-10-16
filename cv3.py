
import cv2
import os

print("Current working directory:",os.getcwd())

display=cv2.imread('hehe.jpg')
fullscreen=cv2.namedWindow('Display Window',cv2.WARP_FILL_OUTLIERS)

if display is None:
    print("Error: Image not found.")
else:
    cv2.imshow('Display Window',display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
