import cv2 as cv

    #--------READİNG İMAGES --------------
image = cv.imread('Photos/Arthur.png') # Your own relative path

cv.imshow('Arthur', image)

cv.waitKey(0)


    #--------- READİNG VİDEOS-------------
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()
