#shape detection
#convert karo gray image mein
#fir edges find karenge fir dimensions find karenge
import cv2

def getContours(img):
   contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
   for cnt in contours:
       area = cv2.contourAREA(cnt)

       if area > 500:
       cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
       peri = cv2.arcLenght(cnt,True)
       approx = cv2.approxPolyDP(cnt,0.02*peri,True)
       objCor = len(approx)
       x, y ,w, h = cv2.boundingRect(approx)
       if objCor == 3:objectType = "Tri"
       elif objCor = 4:
           aspRatio = w/float(h)
           if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
           else : objectType = "rectrangle"
       elif > 4 : objectType = "Circle"
       else:objectType = "None"
       cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
       cv2.putText(imgContour,objectType,
                   (X + (w //2)-10 , y+ (h//2)-10,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),
                    2))


imgContour = img.copy()
imgGray = cv2.cvColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
imgStack = stackImages(0.6,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlur]
                            ))
getContours(imgCanny)