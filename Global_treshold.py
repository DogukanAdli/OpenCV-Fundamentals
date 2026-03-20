import cv2 as cv
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('Photos/Arthur.png')) # Your own relative path

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Converting Blue-Green-Red to Black and White

ret, img_trash = cv.threshold(img_gray, 40, 255, cv.THRESH_BINARY)

cv.imshow('img_gray',img_gray)
cv.imshow('img_trash',img_trash)
cv.waitKey(0)