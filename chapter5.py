#joining images
import numpy as np


def stackImages(scale,imgArray):
    row = len(imgArray)
    cols = len(imgArray[0])

    rowAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowAvailable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2] 

#a problem with this is tht we cannot stack images with diff channels
horizontal = np.hstack(img,img)
vertical = np.vstack(img,img)