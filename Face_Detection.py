import cv2 as cv
import os
import mediapipe as mp

# THİS CODE PUTS A MASK ON YOUR FACE USİNG YOUR WEBCAM.
# You should press lowercase q on your keyboard to interrupt the program.

def rescaleFrame(frame, scale=1):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def img_process(img, face_detection):
    H, W, _ = img.shape
    
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            
            x,y,w,h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            
            x = int(x*W)
            y = int(y*H)
            w = int(w*W)
            h = int(h*H)
            
            img = cv.rectangle(img, (x,y), (x+w, y+h),(150,7, 16), -1)
            cv.circle(img,(x+35,y+40),12,(0,0,0),-1)
            cv.circle(img,(x+100,y+40),12,(0,0,0),-1)
            cv.line(img,(x+67,y+67), (x+67, y+80), (0,0,0),10)
            cv.line(img,(x+30,y+57), (x+30, y+65), (0,0,0),4)
            cv.putText(img, 'SPIDERMAN',(x+8, y+17), cv.FONT_HERSHEY_COMPLEX, 0.6, (0,0,245), thickness=2)
            cv.circle(img, (x+69,y+115), 15,(0,0,0),thickness=5)

            
            #img[y: y+h , x: x+w, :] = cv.blur(img[y: y+h , x: x+w, :],(30,30))
            
            #img = cv.rectangle(img, (x,y), (x+w, y+h),(10,120, 250), 2)
    return img

img_ = cv.imread('Photos/Faces.png')
img = rescaleFrame(img_)


mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    capture = cv.VideoCapture(0)
    ret, frame = capture.read()
    
    while ret:
        frame = img_process(frame, face_detection)
        frame = rescaleFrame(frame,scale=1.5)
        cv.imshow('frame',frame)
        ret, frame = capture.read()
    
        if cv.waitKey(25)&0xFF==ord('q'):
            break
        

    capture.release()

