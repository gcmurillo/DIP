import cv2

imagen = cv2.imread("image.jpg", 1)
cv2.namedWindow("Practica 1", cv2.WINDOW_NORMAL)
cv2.imshow("Practica 1", imagen)
cv2.imwrite("image.jpg", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()