
import cv2

img1 = cv2.imread("image.jpg", 1)

img2 = img1.copy()

rect = cv2.selectROI("ROI Selector", img2)