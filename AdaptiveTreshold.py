import cv2 as cv

img = cv.imread('Photos/Handwritten.jpg')

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

tresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25,30)

cv.imshow('img', img)
cv.imshow('tresh', tresh)

cv.waitKey(0)