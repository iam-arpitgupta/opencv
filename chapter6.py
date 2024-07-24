#color detection
import cv2
def empty(a):
    pass
path = #location or the path of the image
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",#size (620,480)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",19,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",110,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",240,255,empty)
cv2.createTrackbar("Val Min","Trackbars",153,255,empty)
cv2.createTrackbar("Val Max","Trackbars",0,255,empty)

while True:
img = cv2.imread()
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
s_max= cv2.getTrackbarPos("Sat Max,"Trackbars")
v_min = cv2.getTrackbarPos("Hue Min","Trackbars")
v_max = cv2.getTrackbarPos("Val Max","Trackbars")

print(h_min)
cv2.imshow(img)
cv2.imshow("HSV",imgHSV)
cv2.waitKey(0)
lower = np.array([h_min,s_min,v_min])
upper = np.array(h_max,s_max,v_max)
mask = cv2.inrange(imgHSV,lower,upper)
imgResult = cv2.bitwise_and(img,img,mask=mask)