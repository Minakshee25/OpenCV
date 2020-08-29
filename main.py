import cv2
import numpy as np
cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('hands.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def left():
    print("Left Hand detected - ", x1, y1, w1, h1)

def right():
    print("Right hand detected - ", x1, y1, w1, h1)

def both():
    print("Both hands are detected")

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

        l=0
        r=0

        for (x1,y1,w1,h1) in hands:
            if (x1<x):
                cv2.rectangle(roi, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 1)
                l=l+1

            elif ((x1+w1)>x):
                cv2.rectangle(roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 1)
                r=r+1

        if l==r and (l!=0 or r!=0):
            both()
        elif l>r:
            left()
        elif l<r:
            right()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
