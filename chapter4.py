##extracting a single card out of the card of deck

import cv2
import numpy as np

width,height = 250,350
pts1 = np.float([111,219],[287,188],[154,482],[352,440])
pts2 = np.float([0,0],[width,0],[0,height],[width,height])
matrix = cv2.getPerpesctiveTransform(pts1,pts2)
imgOutput = cv2.wrapPerspective(img,matrix,(width,height))

