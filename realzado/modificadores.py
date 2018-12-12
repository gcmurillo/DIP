
import cv2
import numpy as np
from matplotlib import pyplot as plt

def alargamiento(image_path):
    img = cv2.imread(image_path, 0)  # obtener juego en escala de grises
    
    i_min = min(img.ravel())  # mayor y menor nivel del hist
    i_max = max(img.ravel())
    print(i_max)
    print(i_min)

    new_hist = [int((((i - i_min)/(i_max - i_min)) * (255- 0)) + 0) for i in img.flatten()]

    new_image = []
    count = 0
    for i in range(0, img.shape[0]):
        fila = []
        for j in range(0, img.shape[1]):
            fila.append(new_hist[count])
            count += 1 
        new_image.append(fila)

    plt.subplot(1,3,1), plt.hist(img.ravel(),256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(1,3,2), plt.hist(new_hist,256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('New Histogram'), plt.xticks([]), plt.yticks([])
    
    new_image = np.hstack((img, new_image))

    plt.subplot(1,3,3),plt.imshow(new_image, cmap = 'gray')
    plt.title('Images'), plt.xticks([]), plt.yticks([])
    print(min(new_hist))

    plt.show()


#alargamiento('bajo.jpg')

def compresion(image_path, shirnk_max, shrink_min):
    img = cv2.imread(image_path, 0)  # obtener juego en escala de grises
    
    i_min = min(img.ravel())  # mayor y menor nivel del hist
    i_max = max(img.ravel())
    print(i_max)
    print(i_min)

    new_hist = [(((shirnk_max - shrink_min)/(i_max - i_min)) * (i - shrink_min)) + shrink_min  for i in img.flatten()]

    new_image = []
    count = 0
    for i in range(0, img.shape[0]):
        fila = []
        for j in range(0, img.shape[1]):
            fila.append(new_hist[count])
            count += 1 
        new_image.append(fila)

    plt.subplot(1,3,1), plt.hist(img.ravel(),256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(1,3,2), plt.hist(new_hist,256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('New Histogram'), plt.xticks([]), plt.yticks([])
    
    new_image = np.hstack((img, new_image))

    plt.subplot(1,3,3),plt.imshow(new_image, cmap = 'gray')
    plt.title('Images'), plt.xticks([]), plt.yticks([])
    print(min(new_hist))

    plt.show()

#compresion('bajo.jpg', 50, 100)

def desplazamiento(image_path, offset):

    img = cv2.imread(image_path, 0)  # obtener juego en escala de grises

    new_hist = [i + offset  for i in img.flatten()]

    new_image = []
    count = 0
    for i in range(0, img.shape[0]):
        fila = []
        for j in range(0, img.shape[1]):
            fila.append(new_hist[count])
            count += 1 
        new_image.append(fila)

    plt.subplot(1,3,1), plt.hist(img.ravel(),256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('Histogram'), plt.xticks([]), plt.yticks([])

    plt.subplot(1,3,2), plt.hist(new_hist,256,[0,255], color = 'r'), plt.xlim([0,256])
    plt.title('New Histogram'), plt.xticks([]), plt.yticks([])
    
    new_image = np.hstack((img, new_image))

    plt.subplot(1,3,3),plt.imshow(new_image, cmap = 'gray')
    plt.title('Images'), plt.xticks([]), plt.yticks([])
    print(min(new_hist))

    plt.show()

#desplazamiento('bajo.jpg', 50)

def ecualizar(image_path):

    img = cv2.imread(image_path, 0)  # obtener juego en escala de grises
    hist = img.flatten()

    cdf = hist.cumsum()

ecualizar('posa.jpg')