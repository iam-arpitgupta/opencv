import cv2
import numpy as np
img = cv2.imread("resources/IMG_20240226_104412.jpg")
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dialate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,itrerations=1)


cv2.imshow("gray Image",imgGray)
cv2.waitKey(0 )