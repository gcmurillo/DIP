
import cv2
import numpy as np

img = cv2.imread("img.bmp", 1)
cv2.namedWindow("Imagen Original", cv2.WINDOW_NORMAL)

'''rango_colores = [
    ([50,50,255], [50,50,150])
]

for (lower, upper) in rango_colores:
    
    # Creando variables de color
    lower = np.array(lower, dtype='uint8')
    upper = np.array(upper, dtype='uint8')

    b, g, r = cv2.split(img)
    # Creando una mascara con los colores antes determinados
    mask = cv2.inRange(img, lower, upper)
    
    cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
    cv2.imshow("mask", mask)
    output = cv2.bitwise_and(img, img, mask = mask)

    cv2.namedWindow("images", cv2.WINDOW_NORMAL)
    cv2.imshow("images", np.hstack([img, output]))
    cv2.waitKey(0)
'''

imgGRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGRAY = cv2.add(imgGRAY, 50)
cv2.imshow("Imagen Original", imgGRAY)
cv2.waitKey(0)
rect = cv2.imread("img1.bmp")
rectGRAY = cv2.cvtColor(rect, cv2.COLOR_BGR2GRAY)
cv2.imshow("rect", rectGRAY)
cv2.waitKey(0)
extracted = cv2.bitwise_and(imgGRAY, rect)
cv2.imshow("result", extracted)
cv2.waitKey(0)