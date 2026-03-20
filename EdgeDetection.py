import cv2 as cv
import numpy as np

def rescale_Frame(frame, scale=0.70):
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)
    dimensions = (width, heigth)
    return cv.resize(frame, dimensions, cv.INTER_AREA)

img = rescale_Frame(cv.imread('Photos/Arthur.png'))

img_cannny = cv.Canny(img, 50, 100)     # You can play with the numbers to see the difference.

img_dilate = cv.dilate(img_cannny, np.ones((3,3), dtype=np.int8)) # You can play with the numbers to see the difference.

img_erode = cv.erode(img_dilate, np.ones((3,3), dtype=np.int8)) # You can play with the numbers to see the difference.

cv.imshow('img',img)
cv.imshow('img_dilate',img_dilate)
cv.imshow('img_erode',img_erode)
cv.imshow('img_cannny',img_cannny)
cv.waitKey(0)