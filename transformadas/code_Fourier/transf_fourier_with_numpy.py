'''''''''''''''''''''''''''''''''''''''''''''
        PROCESAMIENTO DIGITAL DE IMÁGENES

                LABORATORIO 7
       TRANSFORMADA DE FOURIER CON NUMPY
'''''''''''''''''''''''''''''''''''''''''''''

import cv2
import numpy as np
from matplotlib import pyplot as plt


def inputImg():
    img = None
    while(True):
        ruta = input("\n\tIngrese ruta de la imagen: ")
        img = cv2.imread(ruta,0)
        if (type(img)!=type(None)):
            return img
        else:
            print("\n\tNo se pudo abrir la imagen.\n")

    #return img


while(True):
    print("\n\n************************************************************")
    print("\n\t\tPROCESAMIENTO DIGITAL DE IMÁGENES")
    print("\n\t\t    TRANSFORMADA DE FOURIER")
    print("\n\n************************************************************")

    img = inputImg()



    #Calculo de la transformada de fourier
    f = np.fft.fft2(img)
    #Se centran los valores de frecuencia al eje 0
    fshift = np.fft.fftshift(f)
    #Calculo de la magnitud de la transformada
    magnitud = 20*np.log(np.abs(fshift))


    #Visualización de la imagen de entrada
    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    #Visualización del espectro de magnitud de la imagen de entrada
    plt.subplot(122),plt.imshow(magnitud, cmap = 'gray')
    plt.title('Espectro de Magnitud'), plt.xticks([]), plt.yticks([])
    plt.show()
    
