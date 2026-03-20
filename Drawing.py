import cv2 as cv
import numpy as np

# all this functions also work on videos

blank = np.zeros((500,500,3), dtype='uint8')   # Creates a black empty image.
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[0:100, 300:400] = (0,255,0)
#cv.imshow('Green', blank)    # You can see the image by erasing '#' at the beginning.


# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (200,98,57), thickness=-1)
#cv.imshow('Rectagle', blank) # You can see the image by erasing '#' at the beginning.


# 3. Draw a circle
cv.circle(blank, (250,250), 100, (150,85,190), thickness=-1)
#cv.imshow('Circle', blank) # You can see the image by erasing '#' at the beginning.


# 4. Draw a line
cv.line(blank, (0,500), (500,0), (50,200,120), thickness=5)
cv.line(blank, (0,0), (500,500), (50,200,120), thickness=5)
#cv.imshow('Line', blank)


# 5. Write text
cv.putText(blank, 'You can write anything', (40,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,245), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)

