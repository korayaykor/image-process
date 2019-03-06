import cv2
import numpy as np

filename = 'IMAGE-NAME.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#making image gray scale

gray = np.float32(gray)#much easier to detect in gray.
dst = cv2.cornerHarris(gray,2,3,0.1)


dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.resizeWindow('dst', 600,600)
cv2.imshow('dst',img)#rewrite image
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroWindows()
