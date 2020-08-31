import cv2
import pyautogui

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier('fist.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)

    roi = frame[200:385, 50:600]
    cv2.rectangle(frame, (50, 200), (600, 385), (255, 255, 255), 0)

    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayroi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)

    hands = hand_cascade.detectMultiScale(grayroi, 1.3, 4)
    faces = face_cascade.detectMultiScale(grayframe, 1.3, 4)

    if len(faces)!=0:
        x = faces[0][0]
        y = faces[0][1]
        w = faces[0][2]
        h = faces[0][3]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)

        l=r=0

        for (x1,y1,w1,h1) in hands:
            if (x1<x):
                cv2.rectangle(roi, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 1)
                l=l+1

            elif ((x1+w1)>x):
                cv2.rectangle(roi, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 255), 1)
                r=r+1

        if l==r and (l!=0 or r!=0):
            print("Both hands are detected")
            pyautogui.press('up')
        elif l>r:
            print("Left Hand detected")
            pyautogui.press('left')
        elif l<r:
            print("Right hand detected")
            pyautogui.press('right')

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
