import cv2
image = cv2.imread("image.jpeg")
print("Dimensiones: ", image.shape)
pixel= image[200, 550]
print("RGB: ", pixel)
bright = sum(pixel)/3
print("Nivel de brillo en el pixel 200:500: ", bright)