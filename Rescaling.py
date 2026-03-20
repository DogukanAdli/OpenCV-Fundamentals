import cv2 as cv


def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 
img = cv.imread('Photos/Arthur.png')  # Your own relative path

img_resized = rescaleFrame(img)

cv.imshow('Arthur', img)
cv.imshow('Arthur_resized', img_resized)

cv.waitKey(0)



# To show that also works on videos
capture = cv.VideoCapture(0)    # Usually webcam
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=1.5)

    #cv.imshow('Video', frame)
    cv.imshow('Resized', frame_resized)

    if cv.waitKey(20)&0xFF==ord('q'):  # To quit press lowercase q.
        break
    
capture.release()
cv.destroyAllWindows()
