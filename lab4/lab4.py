
import cv2
cap = cv2.VideoCapture('video1.avi')
cv2.namedWindow("img1", cv2.WINDOW_NORMAL)
cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
cv2.namedWindow("img3", cv2.WINDOW_NORMAL)

n_frame = 0
img1 = None
img2 = None

frames = []

while True:
    ret, frame = cap.read()
    
    if ret:
        if n_frame == 20:
            img = frame
            frames.append(img)
            #cv2.imshow('img1', img)
            #cv2.waitKey(0)
            n_frame = 0
        else:
            n_frame += 1
    else: 
        break
    

for i in range(0, len(frames)):
    img1 = frames[i]
    img2 = frames[-1]

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, binaria1 = cv2.threshold(gray1, 30, 255, cv2.THRESH_BINARY)
    ret, binaria2 = cv2.threshold(gray2, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)

    #img3 = cv2.subtract(img1, img2)
    img3 = cv2.subtract(img1, img2)
    ret, img3 = cv2.threshold(img3, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow("img3", img3)

    cv2.waitKey(0)