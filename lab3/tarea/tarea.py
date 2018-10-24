
import cv2

img1 = cv2.imread("img1.bmp", 1)
img2 = cv2.imread("img2.bmp", 1)
img3 = cv2.imread("img3.bmp", 1)

img4 = cv2.add(img1, img2)
img4 = cv2.add(img4, img3)
cv2.namedWindow("Img1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Img2", cv2.WINDOW_NORMAL)
cv2.namedWindow("Img3", cv2.WINDOW_NORMAL)
cv2.imshow("Img1", img1)
cv2.imshow("Img2", img2)
cv2.imshow("Img3", img3)
cv2.namedWindow("result", cv2.WINDOW_NORMAL)
cv2.imshow("result", img4)
cv2.waitKey(0)