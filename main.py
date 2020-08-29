import cv2
import numpy as np
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hands.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def left():
    print("Left Hand detected - ", x1, y1, w1, h1)
def right():
    print("Right hand detected - ", x1, y1, w1, h1)

while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    roi = frame[200:385, 50:600]
    cv2.rectangle(frame, (50, 200), (600, 385), (255, 255, 255), 0)

    hands = hand_cascade.detectMultiScale(roi, 1.3, 4)
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)

    if len(faces)!=0:
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

        for (x1, y1, w1, h1) in hands:
            if (x1<x):
                left()
            elif ((x1+w1)>x):
                right()
            cv2.rectangle(roi, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 1)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
