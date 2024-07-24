import cv2
print("package Imported")

#img = cv2.imread(#path of the image)
    #output of the image
#cv2.imshow("Output",img)
    #cv2.waitkey

#for the video capture
#cap = cv2.VideoCapture(#path of the video)
#since video is the collection of the frames of the images so we use the loop
#while True:
 #   success, img = cap.read()
 #   cv2.imshow("Video",img)
 #   if cv2.waitkey(1) & 0xFF == ord('q'):
 #       break
# q is used for closinthe video

##using  a web cam -->
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height
cap.set(10,100)#brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
cap.release()



